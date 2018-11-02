import json 
from f5.bigip import ManagementRoot
from pprint import pprint

mgmt = ManagementRoot('172.16.70.105', 'admin', 'password')

pool = mgmt.tm.ltm.pools.pool.load(partition='Common', name='test')
member = pool.members_s.get_collection()

for m in member :
    pprint(m.raw)


