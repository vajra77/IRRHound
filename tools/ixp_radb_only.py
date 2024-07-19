import sys
import json
import time
from urllib.request import urlopen
from irrhound import irrhound


MEMBERS = []

def load_members(ixf_url):
    response = urlopen(ixf_url)
    data = json.loads(response.read())
    for member in data['member_list']:
        name = member['name']
        asnum = member['asnum']
        for conn in member['connection_list']:
            for vlan in conn['vlan_list']:
                asmacro = vlan['ipv4']['asmacro']
        MEMBERS.append({
            'name': name,
            'asnum': asnum,
            'asmacro': asmacro
        })


if __name__ == "__main__":
    load_members(sys.argv[1])
    for member in MEMBERS:
        sources = irrhound.irr_hunt_sources(member.asnum, member.asmacro, None)
        if 'RADB' in sources:
            print(f"Member {member.name} has resources in: {sources}")
        time.sleep(10)
