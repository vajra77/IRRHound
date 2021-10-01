

class Peer:

    def __init__(self, asn: int, asmacro: str, asmacro6: str):
        self._asn = asn
        self._asmacro = asmacro
        self._asmacro6 = asmacro6

    @property
    def asn(self) -> int:
        return self._asn

    @property
    def asmacro(self) -> str:
        return self._asmacro

    @property
    def asmacro6(self) -> str:
        return self._asmacro6