#!/usr/bin/env python
#

import socket
import os
import sys
from ipscan import searchip
from ipscan import get_my_ip

talk_port = 3490
msgsize = 1024


def sendCmd(serverIp,cmd):
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
		break 

	if sock is None:  
		print 'could not open socket'  
		return False 
	try:
		sock.settimeout(5.0)
		sock.connect((serverIp, talk_port))
		#waiting for server 
		data = sock.recv(msgsize)
		print 'Received',data
		#send cmd to server
		sock.send(cmd)
		# wait server 
		data = sock.recv(msgsize)
		print 'report:',data
		#close
		return True
	except socket.error, msg:
		print msg
		return False
	sock.close


myip = get_my_ip()
server = searchip(myip,talk_port)
if server == myip:
	print "no clinet be found"
	sys.exit()
else:
	print "server ip:",server

try:
	while True:
		input    = raw_input("Enter cmd (q to exit): ")
		if input == 'q':
			break
		if not sendCmd(server, input):
			break


except KeyboardInterrupt:
	print "You pressed Ctrl+C"
	sys.exit()

except socket.error:
	print "Couldn't connect to server"
	sys.exit()

	
	