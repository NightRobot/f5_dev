from f5.bigip import ManagementRoot
from pprint import pprint
import time ,os ,logging

# Test management ip address virtual server BIG IP 10.128.1.145
ipaddress = '10.128.1.145'
username = 'admin'
password = 'password'
pool_name = "lab"

# connect to BIGIP management server
mgmt = ManagementRoot(ipaddress, username, password)

# https://<ipaddress>/mgmt/tm/ltm/
ltm = mgmt.tm.ltm

print("---------------------------------------------------")
print ("management server ",ipaddress)
print("---------------------------------------------------")

# REST api => https://<ipaddress>/mgmt/tm/ltm/pool
# Collection pool
pools = mgmt.tm.ltm.pools

# Resource pool
pool = mgmt.tm.ltm.pools.pool

# load pool name 'test' from resource pool
pool_test = pool.load(partition='Common', name=pool_name)

# read log

def readlog(filepath):
    important = []
    keep_phrases = ["ThreadCount"]
    with open(filepath ,'r') as f:
        f = f.readlines()

    for line in f:
        for phrase in keep_phrases:
            if phrase in line:
                important.append(line)
                break


    # pprint(important)
    text = important[len(important)-1]
    # print(text.split(' '))
    data = text.split(' ')
    return data

clock = 5 # sec
compute = 120 # 5 min
deploy = 180 # 6 min
if __name__ == "__main__" :
    # for p in pool_collection :
    now = time.time()
    timer = now + clock
    while(True) :
        now = time.time()
        if now > timer :
            timer += clock
            print("pool name : ",pool_test.name)
            print("loadbalance method : ",pool_test.loadBalancingMode)

            # REST api => https://<ipaddress>/mgmt/tm/ltm/pool/~Common~<pool name>/members
            # Collection member
            members = pool_test.members_s
            # Resource member
            member = pool_test.members_s.members
            print("==> member collection in ",pool_test.name," pool <==")
            member_collection = members.get_collection()
            print(member_collection)
            for m in member_collection :

                # REST api => https://<ipaddress>/mgmt/tm/ltm/pool/~Common~<pool name>/members/~Common~<member name>
                print("name : ",m.name)
                print("address : ",m.address)
                print("ratio : ",m.ratio)
                print("session : ",m.session)
                print("state : ",m.state)

                print("---------------------------------------------------")

                logdata = readlog("thread.log")
                print("update ratio :",logdata[len(logdata)-1])

                ratio = int (logdata[len(logdata)-1])
                m.ratio = ratio
                m.update()
                print("---------------------------------------------------")


            localtime = time.asctime( time.localtime(time.time()) )
            print ("Local current time :", localtime)
            print("---------------------------------------------------")
