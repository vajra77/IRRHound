

class IRRSourceList:
    """
        Static information about IRR registries
    """

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

    _DEFAULT_SOURCE_WEIGHT = {
        'RADB': 0,
        'AFRINIC': 0,
        'ALTDB': 0,
        'APNIC': 3,
        'ARIN': 3,
        'ARIN-NONAUTH': 0,
        'BBOI': 0,
        'BELL': 0,
        'CANARIE': 0,
        'HOST': 0,
        'IDNIC': 0,
        'JPIRR': 0,
        'LACNIC': 3,
        'LEVEL3': 0,
        'NESTEGG': 0,
        'NTTCOM': 0,
        'OPENFACE': 0,
        'PANIX': 0,
        'REACH': 0,
        'RIPE': 3,
        'RIPE-NONAUTH': 0,
        'TC': 0
    }

    def __init__(self):
        pass

    @classmethod
    def default_weight(cls):
        return cls._DEFAULT_SOURCE_WEIGHT.copy()

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
    def rirs_only(cls) -> list:
        return cls.build_list((1,3,4,12,19))

    @classmethod
    def all(cls) -> list:
        return cls._ALL_SOURCES

    @staticmethod
    def build_list(idx: tuple):
        result = []
        for i in idx:
            result.append(IRRSourceLists._ALL_SOURCES[i])
        return result
