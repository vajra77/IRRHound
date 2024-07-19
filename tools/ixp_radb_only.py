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
        asmacro = None
        for conn in member['connection_list']:
            for vlan in conn['vlan_list']:
                if 'as_macro' in vlan['ipv4'].keys():
                    asmacro = vlan['ipv4']['as_macro']
        MEMBERS.append({
            'name': name,
            'asnum': asnum,
            'asmacro': asmacro
        })


if __name__ == "__main__":
    load_members(sys.argv[1])
    with open(sys.argv[2], "w+") as f:
        for member in MEMBERS:
            f.write(f"--- {member['name']} ---")
            try:
                sources = irrhound.irr_hunt_sources(member['asnum'], member['asmacro'], None)
                if 'RADB' in sources:
                    f.write(f"Member {member['name']} has resources in: {sources}")
            except Exception as e:
                f.write(f"ERROR: {e}")
            finally:
                time.sleep(10)
