import sys,getopt
from irrhound.irrhound import irr_hunt_sources


def usage():
    print("Usage: suggest_irr_sources.py -n <ASN> [-m <AS macro>] [-l <AS6 macro>")

def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "n:m:l:", ["asn=", "macro=", "macro6="])

    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    (asn, macro, macro6) = (None,None,None)

    for o, a in opts:
        if o in ("-n", "--asn"):
            asn = a
            if 'AS' in asn:
                asn = asn[2:]
        elif o in ("-m", "--macro"):
            macro = a
        elif o in ("-l", "--macro6"):
            macro6 = a
        else:
            assert False, "unhandled option"

    if not asn:
        print("Error: insufficient arguments")
        usage()
        sys.exit(2)

    suggested = irr_hunt_sources(asn, macro, macro6)
    print("Suggested source list is {}.".format(suggested['sources']))

if __name__ == "__main__":
    main()
