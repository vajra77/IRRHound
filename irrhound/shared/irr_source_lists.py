

class IRRSourceLists:

    _ALL_SOURCES = [
            'RADB',         # id 0
            'AFRINIC',
            'ALTDB',
            'APNIC',
            'ARIN',
            'ARIN-NONAUTH', # id 5
            'BBOI',
            'BELL',
            'CANARIE',
            'HOST',
            'IDNIC',        # id 10
            'JPIRR',
            'LACNIC',
            'LEVEL3',
            'NESTEGG',
            'NTTCOM',       # id 15
            'OPENFACE',
            'PANIX',
            'REACH',
            'RIPE',
            'RIPE-NONAUTH', # id 20
            'TC'
    ]

    @classmethod
    def ripe_region(cls) -> list:
        return cls.build_list((19,20))

    @classmethod
    def default(cls) -> list:
        return cls.build_list((0, 19, 20))

    @classmethod
    def default_extended(cls) -> list:
        return cls.build_list((19, 20, 0, 4, 15))

    @classmethod
    def all(cls) -> list:
        return cls._ALL_SOURCES

    @staticmethod
    def build_list(idx: tuple):
        result = []
        for i in idx:
            result.append(IRRSourceLists._ALL_SOURCES[i])
        return result
