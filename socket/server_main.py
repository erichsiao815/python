#!/usr/bin/env python
#
#
#
# Todo : add thread
#
import socket
import os
import sys
import time
import os.path
import motor
import car


def SrvCommand(cmd):
	result = 'ERROR'
	num = 0
	for str in cmd.split(' '):
		num+=1
	#print "split number {0}".format(num)
	header = cmd.split(' ')[0]
	type = cmd.split(' ')[1]
	
	if  header== "motor":
		if num < 3:
			print "format dont match \n"
			return result

		para = cmd.split(' ')[2]
		
		if  type == 'read':
			result = motor.state()
		elif type == 'write':
			result = motor.ctrl(para)
		elif type == 'getspeed':
			result = motor.getSpeed()
		elif type == 'setspeed':
			result = motor.setSpeed(para)
		else:
			print "motor: ctrl type error"
	elif header== "car":
		if num < 2:
			print "format dont match \n"
			return result

		
		if  type == 'go':
			result = car.ctrl("right",1)
			result = car.ctrl("left",1)
		elif type == 'right':
			result = car.ctrl("right",0)
			result = car.ctrl("left",1)
		elif type == 'left':
			result = car.ctrl("right",1)
			result = car.ctrl("left",0)
		elif type == 'back':
			result = car.ctrl("right",-1)
			result = car.ctrl("left",-1)
		elif type == 'backr':
			result = car.ctrl("right",0)
			result = car.ctrl("left",-1)
		elif type == 'backl':
			result = car.ctrl("right",-1)
			result = car.ctrl("left",0)
		elif type == 'stop':
			result = car.ctrl("right",0)
			result = car.ctrl("left",0)
		else:
			print "car: ctrl type error"
	else:
		print "header error"
	return result


talk_port = 3490
msgsize = 1024
myip = None
print "server start"
sock = None 
#loop through all the results and connect to the first we can
for res in  socket.getaddrinfo(myip, talk_port,
			       socket.AF_UNSPEC,
			       socket.SOCK_STREAM, 
			       0,
			       socket.AI_PASSIVE):
	af, socktype, proto, canonname, sa = res
	try:
		sock = socket.socket(af, socktype, proto) 
	except socket.error, err_msg:  
		print err_msg
		sock = None  
		continue
	try:
		#sock.settimeout(5.0)
		sock.bind(sa)
		sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.listen(5)
	except socket.error, err_msg:  
		print err_msg  
		sock.close()  
		sock = None  
		continue  
	break

if sock is None:  
	print 'could not open socket'  
	sys.exit(1)  
	
try:	
	print "server ready to receive"
	while True:
		(csock, addr) = sock.accept()
		csock.settimeout(5.0)
		print "connection from ",addr
		#hostname = sock.GetHostName()
		cmd = "Im bpi"
		csock.send(cmd)
		#time.sleep(1)
		data = csock.recv(msgsize)
		if data is None:
			print "cmd error"
		else:
			if len(data) <= 0:
				print "ping me ??"
			else:
				print 'Received',data
				data = SrvCommand(data)
				csock.send(data)
		csock.close()


except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()

except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        sys.exit()

except socket.error:
        print "Couldn't connect to server"
        sys.exit()

	