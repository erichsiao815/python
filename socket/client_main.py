#!/usr/bin/env python
#

import socket
import os
import sys
from ipscan import searchip
from ipscan import get_my_ip


talk_port = 3490
msgsize = 1024
myip = get_my_ip()
client = searchip(myip,talk_port)
#print "my ip is ",myip,", client is ",client
if client == myip:
	print "no clinet be found"
	sys.exit()
else:
	print "client ip:",client
	
#loop through all the results and connect to the first we can
for res in  socket.getaddrinfo(client, talk_port,
			       socket.AF_UNSPEC,
			       socket.SOCK_STREAM, 
			       0,
			       socket.AI_PASSIVE):
	af, socktype, proto, canonname, sa = res
	sock = socket.socket(af, socktype, proto) 
	sock.settimeout(30.0)
	sock.connect((client, talk_port))
	#waiting for server 
	data = sock.recv(msgsize)
	print 'Received',data
	#send cmd to server
	cmd    = raw_input("Enter cmd to server: ")
	sock.send(cmd)
	# wait server 
	data = sock.recv(msgsize)
	print 'report:',data
	#close
	sock.close()

