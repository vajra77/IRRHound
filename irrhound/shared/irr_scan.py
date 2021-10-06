from .whois_proxy import WhoisProxy
from .peer import Peer
from .irr_source_list import IRRSourceList


class IRRScan:
    """
        Wrapper class for the entire IRR scan process, peer-based
    """

    def __init__(self, peer: Peer):
        self._peer = peer
        self._routes = {}
        self._source_weight = IRRSourceList.default_weight()
        self._executed = False

    @property
    def peer(self) -> Peer:
        return self._peer

    @property
    def routes(self) -> list:
        return self._routes.values()

    def execute(self) -> None:
        as_list = []

        # expand AS-SET (v4)
        if self.peer.asmacro:
            as_list.extend(WhoisProxy.expand_as_macro(self.peer.asmacro))

        # expand AS-SET (v6)
        if self.peer.asmacro6:
            tmp_list = WhoisProxy.expand_as_macro(self.peer.asmacro6)
            for new_as in tmp_list:         # try to avoid duplicates
                if not (new_as in as_list):
                    as_list.append(new_as)

        # check if peer AS is missing from AS-SET generated list
        if not self.peer.asn in as_list:
            as_list.append(self.peer.asn)

        # find route objects
        for asn in as_list:
            found_routes = WhoisProxy.expand_as(asn)
            for new_route in found_routes:
                # check duplicate route objects
                if new_route.cidr in self._routes.keys():
                    existing_route = self._routes[new_route.cidr]
                    if self._source_is_preferred(new_route.source, existing_route.source):
                        new_route.add_duplicate(existing_route)
                        self._routes[new_route.cidr] = new_route
                        self._increase_source_weight(new_route.source)
                        self._decrease_source_weight(existing_route.source)
                    else:
                        existing_route.add_duplicate(new_route)
                else:
                    self._routes[new_route.cidr] = new_route
                    self._increase_source_weight(new_route.source)

        self._executed = True

    def selected_sources(self) -> list:
        if self._executed:
            result = []
            for route in self._routes.values():
                if not route.source in result:
                    result.append(route.source)
            return result
        else:
            raise Exception("Scan not executed")

    def _source_is_preferred(self, first: str, second: str) -> bool:
        if (first in self._source_weight.keys()) and (second in self._source_weight.keys()):
            return (self._source_weight[first] > self._source_weight[second])
        else:
            return False

    def _increase_source_weight(self, source: str) -> None:
        if source in self._source_weight.keys():
            self._source_weight[source] += 1
        else:
            raise Exception("Unrecognized IRR source: {}".format(source))

    def _decrease_source_weight(self, source: str) -> None:
        if source in self._source_weight.keys():
            self._source_weight[source] -= 1
        else:
            raise Exception("Unrecognized IRR source: {}".format(source))