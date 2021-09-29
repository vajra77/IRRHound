from .filter_toolkit import FilterToolkit
from .peer import Peer


class IRRSourceScan:

    def __init__(self, peer: Peer, source: str):
        self._peer = peer
        self._source = source
        self._ipv4_prefixes = []
        self._ipv6_prefixes = []
        self._executed = False

    @property
    def peer(self) -> Peer:
        return self._peer

    @property
    def source(self) -> str:
        return self._source

    @property
    def ipv4_prefixes(self) -> list:
        return self._ipv4_prefixes.copy()

    @property
    def ipv6_prefixes(self) -> list:
        return self._ipv6_prefixes.copy()

    @property
    def has_entries(self) -> bool:
        if self._executed:
            return (self.has_v4_entries or self.has_v6_entries)
        else:
            return False

    @property
    def has_v4_entries(self) -> bool:
        if self._executed:
            return (len(self._ipv4_prefixes) > 0)
        else:
            return False

    @property
    def has_v6_entries(self) -> bool:
        if self._executed:
            return (len(self._ipv6_prefixes) > 0)
        else:
            return False

    def execute(self):
        self._ipv6_prefixes.clear()
        self._ipv4_prefixes.clear()

        # check for ipv4 prefixes
        as_entries = []
        if self.peer.asmacro:
            as_entries.extend(FilterToolkit.bgpq_expand_as_macro(self.peer.asmacro, self.source))

        if not self.peer.asn in as_entries:
                as_entries.append(self.peer.asn)

        for this_as in as_entries:
                self._ipv4_prefixes.extend(FilterToolkit.bgpq_expand_asn_v4(this_as, self.source))

        # check for ipv6 prefixes
        as6_entries = []

        if self.peer.asmacro6:
            macro = self.peer.asmacro6
        elif self.peer.asmacro:
            macro = self.peer.asmacro
        else:
            macro = None

        if macro:
            as6_entries.extend(FilterToolkit.bgpq_expand_as_macro(macro, self.source))

        if not self.peer.asn in as6_entries:
            as6_entries.append(self.peer.asn)

        for this_as in as6_entries:
            self._ipv6_prefixes.extend(FilterToolkit.bgpq_expand_asn_v6(this_as, self.source))

        self._executed = True