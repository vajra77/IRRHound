

class RouteObject:

    def __init__(self, cidr: str, origin: int, source: str):
        self._cidr = cidr
        if ":" in cidr:
            self._proto = 6
        else:
            self._proto = 4
        self._origin = origin
        self._source = source
        self._duplicates = []

    @property
    def cidr(self) -> str:
        return self._cidr

    @property
    def proto(self) -> int:
        return self._proto

    @property
    def source(self) -> str:
        return self._source

    @property
    def origin(self) -> int:
        return self._origin

    @property
    def has_duplicates(self) -> bool:
        return len(self._duplicates) > 0

    @property
    def duplicates(self) -> list:
        return self._duplicates.copy()

    def add_duplicate(self, other) -> None:
        self._duplicates.append(other)
        self._duplicates.extend(other.duplicates)

    def to_dict(self) -> dict:
        dup_list = []
        if self.has_duplicates:
            for dup in self.duplicates:
                dup_list.append({ 'cidr': dup.cidr, 'origin': dup.origin, 'source': dup.source })
        return { 'cidr': self.cidr, 'origin': self.origin, 'source': self.source, 'duplicates': dup_list }
