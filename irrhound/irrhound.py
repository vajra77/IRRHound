from .shared import IRRHunt

IRR_SOURCES = ['RIPE','RIPE-NONAUTH','RADB','ARIN','APNIC','AFRINIC','NTTCOM']

def irr_hunt_sources(asn, asmacro):
    """
    Returns a list of IRR sources containing objects relatable to
    Autonomous Systems passed as arguments.
    Args:
        irr_hunt_sources (asn, asmacro): main ASN to check for, registered AS-SET to check for
    Returns:
        list
    """


    hunter = IRRHunt(asn, asmacro, IRR_SOURCES)
    
    if asmacro:
        hunter.hunt_asmacro()

    hunter.hunt_asn()

    return hunter.suggested_sources

def irr_hunt_resources(asn, asmacro, source):
    """
    Returns a list of prefixes registered in IRR source
    Args:
        irr_hunt (asn, asmacro, source): main ASN to check for, registered AS-SET to check for, IRR source
    Returns:
        list
    """

    hunter = IRRHunt(asn, asmacro, IRR_SOURCES)

    if asmacro:
        hunter.hunt_asmacro()

    hunter.hunt_asn()
    prefixes = hunter.hunted_prefixes(source)

    return prefixes

