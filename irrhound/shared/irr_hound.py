from .filter_toolkit import FilterToolkit
from .irr_source_scan import IRRSourceScan
from .peer import Peer


class IRRHound:

    def __init__(self, peer: Peer, available_sources: list):
        self._peer = peer
        self._available_sources = available_sources
        self._scanned_sources = []
        self._hunted = False

    @property
    def suggested_sources(self) -> str:
        suggested = []
        if self._hunted:
            for scan in self._scanned_sources:
                suggested.append(scan.source)
        return suggested

    def hunt(self):
        self._scanned_sources.clear()
        for source in self._available_sources:
            scan = IRRSourceScan(self._peer, source)
            scan.execute()
            if scan.has_entries:
                self._scanned_sources.append(scan)
        self._hunted = True

    def retrieve_v4_prefixes(self, source):
        retrieved = []
        if self._hunted:
            for scanned in self._scanned_sources:
                if scanned.source == source:
                    if scanned.has_v4_entries:
                        retrieved.extend(scanned.ipv4_prefixes)
        return retrieved

    def retrieve_v6_prefixes(self, source):
        retrieved = []
        if self._hunted:
            for scanned in self._scanned_sources:
                if scanned.source == source:
                    if scanned.has_v6_entries:
                        retrieved.extend(scanned.ipv6_prefixes)
        return retrieved