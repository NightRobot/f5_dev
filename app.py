from f5.bigip import ManagementRoot
from pprint import pprint

ipaddress = '172.16.70.105'
username = 'admin'
password = 'password'
# connect to BIGIP management server
mgmt = ManagementRoot(ipaddress, username, password)

# https://172.16.70.105/mgmt/tm/ltm/
ltm = mgmt.tm.ltm
print("---------------------------------------------------")
print ("management server ",ipaddress)
print("---------------------------------------------------")
# REST api => https://172.16.70.105/mgmt/tm/ltm/pool
# Collection pool
pools = mgmt.tm.ltm.pools
# Resource pool
pool = mgmt.tm.ltm.pools.pool
pool_collection = pools.get_collection()
for p in pool_collection :
    print("pool name : ",p.name)
    print("loadbalance method : ",p.loadBalancingMode)
    # load pool name 'test' from resource pool
    pool_test = pool.load(partition='Common', name=p.name)
    
    # REST api => https://172.16.70.105/mgmt/tm/ltm/pool/~Common~<pool name>/members
    # Collection member
    members = pool_test.members_s
    # Resource member
    member = pool_test.members_s.members
    print("==> member collection in ",p.name," pool <==")
    member_collection = members.get_collection()
    print(member_collection)
    for m in member_collection :

        # REST api => https://172.16.70.105/mgmt/tm/ltm/pool/~Common~<pool name>/members/~Common~<member name>
        print("name : ",m.name)
        print("address : ",m.address)
        print("ratio : ",m.ratio)
        print("session : ",m.session)
        print("state : ",m.state)
        print("---------------------------------------------------")
        # m.ratio = 2
        # m.update()
    print("---------------------------------------------------")




