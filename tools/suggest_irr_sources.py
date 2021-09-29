import sys
from irrhound.irrhound import irr_hunt_sources


if(len(sys.argv) == 1):
    print("Usage: suggest_irr_sources <AS number> [<AS set v4>] [<AS set v6>]")
    quit()

asn = sys.argv[1]

if 'AS' in asn:
    asn = asn[2:]

if(len(sys.argv) > 2):
    asmacro = sys.argv[2]
else:
    asmacro = None

if(len(sys.argv) > 3):
    asmacro6 = sys.argv[3]
else:
    asmacro6 = None

suggested = irr_hunt_sources(asn, asmacro, asmacro6)

print("Suggested source list is {}.".format(suggested))
