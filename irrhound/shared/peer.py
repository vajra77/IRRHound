

class Peer:

    def __init__(self, name, asn, asmacro, asmacro6, irr_source):
        self._name = name
        self._asn = asn
        self._asmacro = asmacro
        self._asmacro6 = asmacro6
        self._irr_source = irr_source
        self._filters = []

    @property
    def name(self):
        return self._name

    @property
    def asn(self):
        return self._asn

    @property
    def asmacro(self):
        return self._asmacro

    @property
    def irr_source(self):
        return self._irr_source
