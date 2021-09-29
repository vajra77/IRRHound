from .filter_toolkit import FilterToolkit


class IRRHunt:

    def __init__(self, asn, asmacro, sources):
        self._asn = asn
        self._asmacro = asmacro
        self._available_sources = sources
        self._suggested_sources = []
        self._hunted_prefixes = {}

    @property
    def suggested_sources(self):
        return self._suggested_sources.copy()

    def hunted_prefixes(self, source):
        hunted = []
        if source in self._hunted_prefixes.keys():
            hunted = self._hunted_prefixes[source].copy()
        return hunted
    
    def hunt_asmacro(self):
        if self._asmacro:
            for source in self._available_sources:
                as_entries = FilterToolkit.bgpq_expand_as_macro(self._asmacro, source)
                for this_as in as_entries:
                    entries = FilterToolkit.bgpq_expand_asn(this_as, source)
                    if len(entries) > 0:
                        if not source in self._suggested_sources:
                            self._suggested_sources.append(source)
                            self._hunted_prefixes[source] = entries
                        else:
                            self._hunted_prefixes[source].append(entries)

    def hunt_asn(self):
        for source in self._available_sources:
            entries = FilterToolkit.bgpq_expand_asn(self._asn, source)
            if len(entries) > 0:
                if not source in self._suggested_sources:
                    self._suggested_sources.append(source)
                    self._hunted_prefixes[source] = entries
                else:
                    self._hunted_prefixes[source].append(entries)
