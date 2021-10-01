from irrhound.shared import IRRScan, Peer


def test_scan():

    peer = Peer(12637, 'AS12637:AS-CUSTOMERS', None)

    scan = IRRScan(peer)
    scan.execute()
    selected = scan.selected_sources()
    print("Suggested source list is: {}".format(selected))

    assert len(selected) > 0

def test_routes():

    peer = Peer(12637, 'AS12637:AS-CUSTOMERS', None)
    scan = IRRScan(peer)
    scan.execute()
    for route in scan.routes:
        print("Route: {} with origin AS{} [{}]".format(route.cidr, route.origin, route.source))

    assert len(scan.routes) > 0
