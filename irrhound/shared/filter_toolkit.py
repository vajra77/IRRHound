import os
import sys
import json
import uuid

from .peer import Peer
from .network_prefix import NetworkPrefix


class FilterToolkit:

    def __init__(self):
        self._rpki_cache = {}
        pass

    @staticmethod
    def bgpq_expand_asn_v4(asn: str, source: str) -> list:
        entries = []
        filename = FilterToolkit._get_random_filename()
        cmd = "bgpq3 -4 -S {} -j AS{} > {}".format(source, asn, filename)
        if os.system(cmd) != 0:
            raise Exception("Error in execution of bgpq3")
        with open(filename) as f:
            data = json.load(f)
        f.close()
        os.remove(filename)
        for net in data["NN"]:
            entries.append(NetworkPrefix.make(net['prefix'], asn, 0, 'irr'))
        return entries

    @staticmethod
    def bgpq_expand_asn_v6(asn: str, source: str) -> list:
        entries = []
        filename = FilterToolkit._get_random_filename()
        cmd = "bgpq3 -6 -S {} -j AS{} > {}".format(source, asn, filename)
        if os.system(cmd) != 0:
            raise Exception("Error in execution of bgpq3")
        with open(filename) as f:
            data = json.load(f)
        f.close()
        os.remove(filename)
        for net in data["NN"]:
            entries.append(NetworkPrefix.make(net['prefix'], asn, 0, 'irr'))
        return entries

    @staticmethod
    def bgpq_expand_as_macro(macro: str, source: str) -> list:
        entries = []
        filename = FilterToolkit._get_random_filename()
        cmd = "bgpq3 -3 -t -S {} -j {} > {}".format(source, macro, filename)
        if os.system(cmd) != 0:
            raise Exception("Error in execution of bgpq3")
        with open(filename) as f:
            data = json.load(f)
        f.close()
        os.remove(filename)
        for asn in data["NN"]:
            entries.append(str(asn))
        return entries

    @staticmethod
    def _get_random_filename():
        return "/tmp/irr-{}.json".format(uuid.uuid4().hex)