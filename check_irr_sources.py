import sys
from irrhound import irr_hunt


asn = sys.argv[1]
if(len(sys.argv) > 2):
    asmacro = sys.argv[2]
else:
    asmacro = False

suggested = irr_hunt(asn, asmacro)

print("Suggested source list is {}.".format(suggested))
