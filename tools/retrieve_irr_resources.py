import sys,getopt
from irrhound.irrhound import irr_hunt_routes

def usage():
    print("Usage: retrieve_irr_resources.py -n <ASN> [-m <AS macro>] [-l <AS-MACRO6>]")

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
        print("Error: insufficient arguments", file=sys.stderr)
        usage()
        sys.exit(2)

    try:
        retrieved = irr_hunt_routes(asn, macro, macro6)
    except Exception as err:
        print("Error while retrieving resources: {}".format(err), file=sys.stderr)
    else:
        print("# Resources for AS{}:".format(asn))
        for route in retrieved['routes']:
            print("{} with origin AS{} [{}]".format(route['cidr'], route['origin'], route['source']))
            if len(route['duplicates']) > 0:
                for dup in route['duplicates']:
                    print("--> [DUP] {} with origin AS{} [{}]".format(dup['cidr'], dup['origin'], dup['source']))

if __name__ == "__main__":
    main()