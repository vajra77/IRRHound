from ipaddress import IPv4Network, IPv6Network


class NetworkPrefix:

    def __init__(self, prefix, version, origin, maxlen, source):
        self._prefix = prefix
        self._version = version
        self._origin = origin
        self._maxlen = maxlen
        self._source = source

    @property
    def prefix(self):
        return self._prefix

    @property
    def network(self):
        return self.prefix.network_address

    @property
    def mask(self):
        return self.prefix.prefixlen

    @property
    def maxlen(self):
        return self._maxlen

    @property
    def version(self):
        return self._version

    @property
    def origin(self):
        return self._origin

    @property
    def source(self):
        return self._source

    def hash(self):
        return self._network

    # spans only checks supernet
    def spans(self, other) -> bool:
        if self.version == other.version:
            return self.prefix.supernet_of(other.prefix)
        else:
            return False

    # covers checks supernet and maxlen inclusion
    def covers(self, other) -> bool:
        if self.version == other.version:
            return(self.prefix.supernet_of(other.prefix) and (int(self._maxlen) <= other.mask))
        else:
            return False

    @classmethod
    def make(cls, pfx_str, origin, maxlen, source):
        if ':' in pfx_str:
            return cls(IPv6Network(pfx_str),6, origin, maxlen, source)
        else:
            return cls(IPv4Network(pfx_str),4, origin, maxlen, source)