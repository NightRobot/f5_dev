from f5.bigip import ManagementRoot
from pprint import pprint
ipaddress = '172.16.70.105'
username = 'admin'
password = 'password'
# connect to BIGIP management server
mgmt = ManagementRoot(ipaddress, username, password)

# https://172.16.70.105/mgmt/tm/ltm/
ltm = mgmt.tm.ltm

# REST api => https://172.16.70.105/mgmt/tm/ltm/pool
# Collection pool
pools = mgmt.tm.ltm.pools
# Resource pool
pool = mgmt.tm.ltm.pools.pool

# load pool name 'test' from resource pool
pool_test = pool.load(partition='Common', name='test')

# REST api => https://172.16.70.105/mgmt/tm/ltm/pool/~Common~test/members
# Collection member
members = pool_test.members_s
# Resource member
member = pool_test.members_s.members

member_collection = members.get_collection()
for m in member_collection :
    pprint(m.name)

member1 = pool_test.members_s.members.load(partition='Common', name='172.16.70.105:22')
print(member1.name)

