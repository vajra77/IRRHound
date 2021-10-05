

class RouteObject:
    """
        Wraps information of a retrieved ROUTE/ROUTE6 object:

        cidr: network prefix in CIDR notation
        proto: IP protocol version [4|6]
        source: IRR source of retrieved object
        origin: originating ASN
        duplicates: (optional) list of duplicate objects from different IRR sources

    """

    def __init__(self, cidr: str, origin: int, source: str):
        self._cidr = cidr
        if ":" in cidr:
            self._proto = 6
        else:
            self._proto = 4
        self._origin = origin
        self._source = source
        self._duplicates = []

    # returns prefix as string in CIDR notation
    @property
    def cidr(self) -> str:
        return self._cidr

    # returns proto version as integer
    @property
    def proto(self) -> int:
        return self._proto

    # returns IRR source as string
    @property
    def source(self) -> str:
        return self._source

    # returns origin ASN as integer
    @property
    def origin(self) -> int:
        return self._origin

    # check if object stores information about duplicates
    @property
    def has_duplicates(self) -> bool:
        return len(self._duplicates) > 0

    # returns list of duplicate objects
    @property
    def duplicates(self) -> list:
        return self._duplicates.copy()

    # add a duplicate object to duplicates list
    def add_duplicate(self, other) -> None:
        self._duplicates.append(other)
        self._duplicates.extend(other.duplicates)

    # returns object as a formatted dictionary
    def to_dict(self) -> dict:
        dup_list = []
        if self.has_duplicates:
            for dup in self.duplicates:
                dup_list.append({ 'cidr': dup.cidr, 'origin': dup.origin, 'source': dup.source })
        return { 'cidr': self.cidr, 'origin': self.origin, 'source': self.source, 'duplicates': dup_list }
