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
server = searchip(myip,talk_port)
#print "my ip is ",myip,", server is ",server
if server == myip:
	print "no clinet be found"
	sys.exit()
else:
	print "server ip:",server

sock = None
for res in  socket.getaddrinfo(None, talk_port,
			       socket.AF_UNSPEC,
			       socket.SOCK_STREAM, 
			       0,
			       socket.AI_PASSIVE):
	af, socktype, proto, canonname, sa = res
	try:
		sock = socket.socket(af, socktype, proto) 
	except socket.error, msg:  
		sock = None  
		continue  
	try:
		sock.settimeout(5.0)
		sock.connect((server, talk_port))
	except socket.error, msg:  
		sock.close()  
		sock = None  
		continue  
 
	#waiting for server 
	data = sock.recv(msgsize)
	print 'Received',data
	#send cmd to server
	cmd    = raw_input("Enter cmd (send to server): ")
	sock.send(cmd)
	# wait server 
	data = sock.recv(msgsize)
	print 'report:',data
	#close
	sock.close()
	break 


if sock is None:  
	print 'could not open socket'  
	sys.exit(1)  

try:
	sys.exit()

except KeyboardInterrupt:
	print "You pressed Ctrl+C"
	sys.exit()

except socket.gaierror:
	print 'Hostname could not be resolved. Exiting'
	sys.exit()

except socket.error:
	print "Couldn't connect to server"
	sys.exit()

	
	