from .shared import IRRScan, Peer


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

    scan = IRRScan(peer)
    try:
        scan.execute()
    except:
        raise 'Error while scanning IRR sources'

    return scan.selected_sources()

def irr_hunt_resources(asn, asmacro, asmacro6):
    """
    Returns a list of prefixes registered in IRR source
    Args:
        irr_hunt (asn, asmacro, source): main ASN to check for, registered AS-SET to check for, IRR source
    Returns:
        list
    """
    peer = Peer(asn, asmacro, asmacro6)
    scan = IRRScan(peer)
    try:
        scan.execute()
    except:
        raise 'Error while scanning IRR sources'

    return scan.routes