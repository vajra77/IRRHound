from .shared import FilterToolkit, NetworkPrefix


def irr_hunt(asn, asmacro):
    """
    Returns a list of IRR sources containing objects relatable to
    Autonomous Systems passed as arguments.
    Args:
        irr_hunt (asn, asmacro): main ASN to check for, registered AS-SET to check for
    Returns:
        list
    """

    IRR_SOURCES = [ 'RIPE', 'RIPE-NONAUTH', 'RADB', 'ARIN', 'NTTCOM' ]
    suggested = []

    for source in IRR_SOURCES:
        if asmacro:
            entries = FilterToolkit.bgpq_expand_as_macro(asmacro, source)
            if len(entries) > 0:
                #print("Found {} entries for {} in {}".format(len(entries), asmacro, source))
                if not source in suggested:
                    suggested.append(source)

        entries = FilterToolkit.bgpq_expand_asn(asn, source)
        if len(entries) > 0:
            #print("Found {} entries for AS{} in {}".format(len(entries), asn, source))
            if not source in suggested:
                suggested.append(source)
    return suggested
