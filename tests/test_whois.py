from irrhound.shared import WhoisProxy


def test_whois_expand_as():

     asn = 137

     objects = WhoisProxy.expand_as(asn)

     for route in objects:
         print("P: {} from source {}".format(route.cidr, route.source))

     assert (len(objects) > 0)

