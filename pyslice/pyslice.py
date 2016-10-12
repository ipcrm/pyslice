#!/usr/bin/env python

from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client
import re

class PySlice:
  def __init__(self):
    pass

  def authenticate(self,cvalues):
    self.nova = client.Client("2.1", cvalues['username'], cvalues['password'], cvalues['tenant'], cvalues['auth_url'])

  def get_floating_host_entries(self,type='standard'):
    for server in self.nova.servers.list():
      server_info = dict()
      name = server.name

      if not re.search('network', name):
        ips=self.nova.servers.ips(server)
        for network in ips:
          if len(ips[network]) > 1:
            floating_ip = ips[network][1]['addr']
          else:
            print(ips)

        if type == 'standard':
          print ( "{} {} {}".format(floating_ip, name, name.split('.')[0]) )
        elif type == 'puppet':
          print ( "host{'%s': ensure => 'present', ip => '%s', host_aliases => ['%s'] }" % (name,floating_ip,name.split('.')[0]) )
        else:
          print ( "Unknown type requested" )


