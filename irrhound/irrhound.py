from .shared import IRRHound, Peer

IRR_SOURCES = ['RIPE','RIPE-NONAUTH','RADB','ARIN','APNIC','AFRINIC','NTTCOM']

def irr_hunt_sources(asn, asmacro, asmacro6):
    """
    Returns a list of IRR sources containing objects relatable to
    Autonomous Systems passed as arguments.
    Args:
        irr_hunt_sources (asn, asmacro): main ASN to check for, registered AS-SET to check for
    Returns:
        list
    """

    peer = Peer(asn, asmacro, asmacro6)

    hound = IRRHound(peer, IRR_SOURCES)
    hound.hunt()

    return hound.suggested_sources

def irr_hunt_v4_resources(asn, asmacro, source):
    """
    Returns a list of prefixes registered in IRR source
    Args:
        irr_hunt (asn, asmacro, source): main ASN to check for, registered AS-SET to check for, IRR source
    Returns:
        list
    """
    peer = Peer(asn, asmacro, None)
    hound = IRRHound(peer, IRR_SOURCES)
    hound.hunt()
    retrieved = hound.retrieve_v4_prefixes(source)
    return retrieved
