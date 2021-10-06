from ipwhois.net import Net
from ipwhois.asn import ASNOrigin
from .route_object import RouteObject

import os
import json
import uuid

DUMMY_NET = "193.201.40.0"


class BGPQException(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return "bgpq4 error triggered by '{}'.".format(self.message)
        else:
            return "undefined bgpq4 error."

class WhoisProxy:
    """
        Wraps WHOIS operations, relies on bgpq4 and ipwhois
    """
    def __init__(self):
        pass

    # expands an AS-SET into a list of AS numbers, relies on bgpq3
    @staticmethod
    def expand_as_macro(macro: str) -> list:
        entries = []
        filename = WhoisProxy._get_random_tmpfile()
        cmd = "bgpq4 -h whois.radb.net -t -j {} > {}".format(macro, filename)
        if os.system(cmd) != 0:
            raise BGPQException(macro)
        with open(filename) as f:
            data = json.load(f)
        f.close()
        os.remove(filename)
        for asn in data["NN"]:
            entries.append(int(asn))
        return entries

    # expand an ASN into a list of ROUTE/6 objects
    @staticmethod
    def expand_as(asn: int) -> list:
        result = []
        mynet = Net(DUMMY_NET)
        obj = ASNOrigin(mynet)
        lookup = obj.lookup("AS{}".format(asn))

        for net in lookup['nets']:
            cidr = net['cidr']
            source = net['source'].upper() # some records have lowercase source
            route = RouteObject(cidr, asn, source)
            result.append(route)

        return result

    # internal use, required for temporary bgpq4 output storage
    @staticmethod
    def _get_random_tmpfile():
        return "/tmp/irr-{}.json".format(uuid.uuid4().hex)



