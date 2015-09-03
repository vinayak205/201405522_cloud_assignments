#!/usr/bin/python

"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
from mininet.topolib import TreeTopo
x = 0
y = 0
total_host = x*y
switches = []
hosts = []
links = []
switchesLink = []
def emptyNet():

    "Create an empty network and add nodes to it."

    net = Mininet( autoStaticArp=True )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' ) 
    for i in range(1,total_hosts+1):
	if i%2 == 0:
	    hosts.append(net.addHost('h'+str(i), ip='10.0.0.'+str(i)))
	else:
	    hosts.append(net.addHost('h'+str(i), ip='9.0.0.'+str(i)))
    info( '*** Adding switch\n' )    
    for i in range(1,y+1):
	switches.append(net.addSwitch('s'+str(i)))

    info( '*** Creating links\n' )
    #net.addLink( h1, s3 )
    #net.addLink( h2, s3 )
    temp_ind = 0
    ind = 0
    for i in range(len(switches)):
	#links.append(net.addLink(hosts[2*i], switches[i], cls=TCLink))
	#links.append(net.addLink(hosts[(2*i) +1], switches[i], cls=TCLink))
	if temp_ind < total_hosts:
	    for j in range(temp_ind, temp_ind+x):
		links.append(net.addLink(hosts[j], switches[i], cls=TCLink))
		ind = j
	    ind = ind + 1
	    temp_ind = ind
	    if i > 0:
	        switchesLink.append(net.addLink(switches[i-1], switches[i], cls=TCLink))
    info(' ******Allocating Bandwidths\n')
    for i in range(len(links)):
	if i%2 == 0:
	    links[i].intf1.config(bw=1)
	else:
	    links[i].intf1.config(bw=2)	
    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    x = raw_input("Enter Number of Hosts:")
    y = raw_input("Enter Number of Switches:")
    x = int(x)
    y = int(y)
    total_hosts = x*y
    emptyNet()
