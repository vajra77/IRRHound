import sys,getopt
from irrhound.irrhound import irr_hunt_v6_resources, irr_hunt_v4_resources

def usage():
    print("Usage: retrieve_irr_resources.py -s <source> -p <proto> -n <ASN> [-m <AS macro>]")

def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:p:n:m:", ["source=", "proto=", "asn=", "macro="])

    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    (source, proto, asn, macro) = (None,None,None,None)

    for o, a in opts:
        if o in ("-s", "--source"):
            source = a
        elif o in ("-p", "--proto"):
            proto = a
        elif o in ("-n", "--asn"):
            asn = a
            if 'AS' in asn:
                asn = asn[2:]
        elif o in ("-m", "--macro"):
            macro = a
        else:
            assert False, "unhandled option"

    if not source or not asn or not proto:
        print("Error: insufficient arguments")
        usage()
        sys.exit(2)

    if proto == '4':
        retrieved = irr_hunt_v4_resources(asn, macro, source)
    elif proto == '6':
        retrieved = irr_hunt_v6_resources(asn, macro, source)
    else:
        assert False, "unrecognized protocol"

    print("# Resources for AS{} from {} IRR".format(asn, source))
    for prefix in retrieved:
        print("{} with origin AS{}".format(prefix.prefix, prefix.origin))


if __name__ == "__main__":
    main()