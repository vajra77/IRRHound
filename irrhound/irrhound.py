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

    IRR_SOURCES = [ 'RIPE', 'RIPE-NONAUTH', 'RADB', 'ARIN', 'NTTCOM', 'APNIC', 'AFRINIC' ]
    suggested = []

    if asmacro:
        for source in IRR_SOURCES:
            print("--- Check for {} in {}".format(asmacro, source))
            as_entries = FilterToolkit.bgpq_expand_as_macro(asmacro, source)
            for this_as in as_entries:
                entries = FilterToolkit.bgpq_expand_asn(this_as, source)
                if len(entries) > 0:
                    print("Found {} entries for AS{} from {} in {}".format(len(entries), this_as, asmacro, source))
                    if not source in suggested:
                        suggested.append(source)

    for source in IRR_SOURCES:
        print("--- Check for AS{} in {}".format(asn, source))
        entries = FilterToolkit.bgpq_expand_asn(asn, source)
        if len(entries) > 0:
            print("Found {} entries for AS{} in {}".format(len(entries), asn, source))
            if not source in suggested:
                suggested.append(source)

    return suggested
