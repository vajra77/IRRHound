import os
import sys
import json
import uuid

from .peer import Peer
from .network_prefix import NetworkPrefix


class FilterToolkit:

    def __init__(self):
        self._rpki_cache = {}
        pass

    def update_rpki_cache(self, filename) -> None:
        with open(filename) as fp:
            line = fp.readline()
            while line:
                (stras, strprefix, strmaxlen) = line.split(",")
                asn = stras.strip("AS")
                prefix = NetworkPrefix.make(strprefix, asn, strmaxlen, 'rpki')
                if stras in self._rpki_cache.keys():
                    self._rpki_cache[stras].append(prefix)
                else:
                    self._rpki_cache[stras] = [ prefix ]
                line = fp.readline()
        fp.close()

    def rpki_cache_fetch(self, asn) -> list:
        selected = []
        stras = "AS{}".format(asn)
        if stras in self._rpki_cache.keys():
            selected.extend(self._rpki_cache[stras])
        return selected

    def expand_networks_for_peer(self, peer: Peer, version: int) -> list:
        selected = []
        if peer.asmacro:
            as_set = self.bgpq_expand_as_macro(peer.asmacro, peer.irr_source)
        else:
            as_set = [ peer.asn ]

        # expand IRR data and match against ROAs
        for asn in as_set:
            roa_set = self.rpki_cache_fetch(asn)
            for entry in self.bgpq_expand_asn(asn, peer.irr_source):
                uncovered = True
                for roa in roa_set:
                    if roa.covers(entry):
                        uncovered = False
                        break
                if uncovered:
                    selected.append(entry)
            selected.extend(roa_set)
        return selected

    @staticmethod
    def bgpq_expand_asn(asn: str, source: str) -> list:
        entries = []
        filename = FilterToolkit._get_random_filename()
        cmd = "bgpq3 -4 -S {} -j AS{} > {}".format(source, asn, filename)
        os.system(cmd)
        with open(filename) as f:
            data = json.load(f)
        f.close()
        os.remove(filename)
        for net in data["NN"]:
            entries.append(NetworkPrefix.make(net['prefix'], asn, 0, 'irr'))
        return entries

    @staticmethod
    def bgpq_expand_as_macro(macro: str, source: str) -> list:
        entries = []
        filename = FilterToolkit._get_random_filename()
        cmd = "bgpq3 -3 -t -S {} -j {} > {}".format(source, macro, filename)
        os.system(cmd)
        with open(filename) as f:
            data = json.load(f)
        f.close()
        os.remove(filename)
        for asn in data["NN"]:
            entries.append(str(asn))
        return entries

    @staticmethod
    def _get_random_filename():
        return "/tmp/irr-{}.json".format(uuid.uuid4().hex)
