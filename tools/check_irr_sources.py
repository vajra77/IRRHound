import sys
from irrhound import irr_hunt



if(len(sys.argv) == 1):
    print("Usage: check_irr_souces <AS number> [<AS set>]")
    quit()

asn = sys.argv[1]
if(len(sys.argv) > 2):
    asmacro = sys.argv[2]
else:
    asmacro = False

suggested = irr_hunt(asn, asmacro)

print("Suggested source list is {}.".format(suggested))
