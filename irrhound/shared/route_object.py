

class RouteObject:

    def __init__(self, cidr: str, origin: int, source: str):
        self._cidr = cidr
        if ":" in cidr:
            self._proto = 6
        else:
            self._proto = 4
        self._origin = origin
        self._source = source

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

