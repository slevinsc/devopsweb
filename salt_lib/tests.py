"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import salt
systeminfo = [
    'cpu_model', 'cpuarch', 'defaultencoding', 'defaultlanguage', 'domain', 'fqdn', 'host', 'id', 'ipv4', 'kernel', 'kernelrelease',
    'localhost', 'mem_total', 'name', 'nodename', 'num_cpus',  'os', 'os_family', 'oscodename', 'osfullname', 'osrelease',  'roles']
client = salt.client.LocalClient()
# for line in systeminfo:
    # print line
   # ret = client.cmd('*', 'grains.item', line)
   # print ret


def get_host_list():
    host_dict = {}
    ret = client.cmd('*', 'test.ping', '')
    id = 1
    for key in ret:
        host_list = {id: key}
        host_dict.update(host_list)
        id = id + 1
    return host_dict


def get_grains_item():
    host_dict = get_host_list()
    print len(systeminfo)
    for host in host_dict:
        # pass

        for line in systeminfo:
            # print type(systeminfo[id])
            #print line
            ret = client.cmd(host_dict[host], 'grains.item', [line])
            if ret[host_dict[host]]:
                print ret

get_grains_item()
