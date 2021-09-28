class Connection:

    def __init__(self, proto, address, asmacro, maxprefix):
        self._proto = proto
        self._address = address
        self._asmacro = asmacro
        self._maxprefix = maxprefix

    @property
    def proto(self):
        return self._proto

    @property
    def address(self):
        return self._address

    @property
    def asmacro(self):
        return self._asmacro

    @property
    def maxprefix(self):
        return self._maxprefix
