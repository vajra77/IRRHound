import sys
from irrhound.irrhound import irr_hunt_sources


if(len(sys.argv) == 1):
    print("Usage: suggest_irr_souces <AS number> [<AS set>]")
    quit()

asn = sys.argv[1]

if 'AS' in asn:
    asn = asn[2:]

if(len(sys.argv) > 2):
    asmacro = sys.argv[2]
else:
    asmacro = False

suggested = irr_hunt_sources(asn, asmacro)

print("Suggested source list is {}.".format(suggested))
