#!/usr/bin/env python
#

import socket
import os
import sys
from ipscan import searchip
from ipscan import get_my_ip
from directionkey import dirkey
import time
from threading import Thread

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
		print 'srv name:',data
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
# into car mode
def carmode(serverIp):
	key = dirkey()
	#key.start()
	taskfd = Thread(target=key.recive_event, args=())
	taskfd.start()
	print "into car mode"
	stopneed = False
	while True:
		cmd = None
		if key.key_leave:
			print "got leave key"
			#key.exit()
			cmd = "car stop"
			sendCmd(serverIp, cmd)
			# make sure cmd is recived
			return
		elif key.key_up:
			stopneed = True
			if key.key_right:
				cmd = "car right"
			elif key.key_left:
				cmd = "car left"
			else:
				cmd = "car go"
		elif key.key_down:
			stopneed = True
			if key.key_right:
				cmd = "car bright"
			elif key.key_left:
				cmd = "car bleft"
			else:
				cmd = "car back"
		elif stopneed :
			cmd = "car stop"
			stopneed = False
		if cmd is not  None:
			sendCmd(serverIp, cmd)
		time.sleep(0.1)
###################################################
myip = get_my_ip()
server = searchip(myip,talk_port)
if server == myip:
	print "no server be found"
	sys.exit()
else:
	print "server ip:",server

try:
	while True:
		keyin    = raw_input("Enter cmd (q to exit): ")
		if keyin == 'q':
			break
		elif keyin == "carmode":
			carmode(server)
		else:
			if not sendCmd(server, keyin):
			      break


except KeyboardInterrupt:
	print "You pressed Ctrl+C"
	sys.exit()

except socket.error:
	print "Couldn't connect to server"
	sys.exit()

	
	