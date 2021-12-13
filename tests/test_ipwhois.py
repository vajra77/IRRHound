from ipwhois.net import Net
from ipwhois.asn import ASNOrigin


def test_ipwhois():
     DUMMY_NET = "193.201.40.0"
     mynet = Net(DUMMY_NET)
     obj = ASNOrigin(mynet)
     lookup = obj.lookup('AS137')
     for net in lookup['nets']:
         print(net)