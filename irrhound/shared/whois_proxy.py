from ipwhois.net import Net
from ipwhois.asn import ASNOrigin
from .route_object import RouteObject

import os
import json
import uuid

DUMMY_NET = "193.201.40.0"


class WhoisProxy:

    def __init__(self):
        pass

    @staticmethod
    def expand_as_macro(macro: str) -> list:
        entries = []
        filename = WhoisProxy._get_random_tmpfile()
        cmd = "bgpq4 -h whois.radb.net -t -j {} > {}".format(macro, filename)
        if os.system(cmd) != 0:
            raise Exception("Error in execution of bgpq4")
        with open(filename) as f:
            data = json.load(f)
        f.close()
        os.remove(filename)
        for asn in data["NN"]:
            entries.append(asn)
        return entries

    @staticmethod
    def expand_as(asn: int) -> list:
        result = []
        mynet = Net(DUMMY_NET)
        obj = ASNOrigin(mynet)
        lookup = obj.lookup("AS{}".format(asn))

        for net in lookup['nets']:
            cidr = net['cidr']
            route = RouteObject(net['cidr'], asn, net['source'])
            result.append(route)

        return result

    @staticmethod
    def _get_random_tmpfile():
        return "/tmp/irr-{}.json".format(uuid.uuid4().hex)
