from fabric.api import env

host1 = 'root@10.87.65.122'
host2 = 'root@10.87.65.18'
host3 = 'root@10.87.65.19'

router_asn = 64512

host_build = 'root@10.87.65.122'

env.roledefs = {
    'all': [host1,host2,host3],
    'cfgm': [host1],
    'openstack': [host1],
    'control': [host1],
    'compute': [host1,host2,host3],
    'collector': [host1],
    'webui': [host1],
    'database': [host1],
    'build': [host_build],
    'storage-master': [host1],
    'storage-compute': [host1],
}

env.openstack_admin_password = 'c0ntrail123'

env.hostnames = {
    host1: 'a0s1',
}

env.passwords = {
    host1: 'c0ntrail123',
    host2: 'c0ntrail123',
    host3: 'c0ntrail123',
    host_build: 'c0ntrail123',
}

minimum_diskGB = 50

bond= {
    host2 : { 'name': 'bond0', 'member': ['nfp_p0','nfp_p1'], 'mode': '802.3ad', 'xmit_hash_policy': 'layer3+4' },
    host3 : { 'name': 'bond0', 'member': ['nfp_p0','nfp_p1'], 'mode': '802.3ad', 'xmit_hash_policy': 'layer3+4' },
}

control_data = {
    host1 : { 'ip': '172.31.255.1/24', 'gw' : '172.31.255.1', 'device': 'eth1' },
    host2 : { 'ip': '172.31.255.2/24', 'gw' : '172.31.255.1', 'device': 'bond0' },
    host3 : { 'ip': '172.31.255.3/24', 'gw' : '172.31.255.1', 'device': 'bond0' },
}

env.ns_agilio_vrouter = {
    host2: {'huge_page_alloc': '24G', 'huge_page_size': '1G', 'coremask': '2,4', 'pinning_mode': 'auto:combine'},
    host3: {'huge_page_alloc': '24G', 'huge_page_size': '1G', 'coremask': '2,4', 'pinning_mode': 'auto:combine'}
}
