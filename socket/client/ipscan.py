#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
from threading import Thread
import fcntl
import struct

ip_exist = [0]*256	#list type
# We also put in some error handling for catching errors
def _get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', ifname[:15])
            )[20:24])

def get_my_ip():
        ip = socket.gethostbyname(socket.gethostname())
        if ip.startswith("127.") :
            interfaces = ["eth0","eth1","eth2","wlan0","wlan1","wifi0","ath0","ath1","ppp0"]
            for ifname in interfaces:
		  try:
			ip = _get_interface_ip(ifname)
			break;
		  except IOError:
			pass
        return ip

def _pingIp(number, ipaddr,port):
	#print "Please wait, scanning remote host ", ipaddr
	ip_exist[number] = 0;
	remoteServerIP  = socket.gethostbyname(ipaddr)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(3.0)
	result = sock.connect_ex((remoteServerIP, int(port)))
	if result == 0:
	       # print "IP {0}:Port  {1} \t Open".format( remoteServerIP, port)            #print "IP %s:Port  %s \t Open"%(remoteServerIP,port)
	       ip_exist[number] = 1;
	sock.close() 
	#print "close socket ", ipaddr
	
def searchip(serverIp, scanPort):
	taskid = {}	#list type
	baseip = {}	#list type
	clientIp = serverIp
	baseip[0] = serverIp.split('.')[0]
	baseip[1] = serverIp.split('.')[1]
	baseip[2] = serverIp.split('.')[2]
	baseip[3] = serverIp.split('.')[3]
	for ip in range(2,256):
		#if int(baseip[3]) != ip:
			str_newip = "{0}.{1}.{2}.{3}".format(baseip[0],baseip[1],baseip[2],ip)	#newip = "%s.%s.%s.%d" %(baseip[0],baseip[1],baseip[2],ip)
			taskid[ip] = Thread(target=_pingIp, args=(ip,str_newip,scanPort))
			#time.sleep(0.1)
			taskid[ip] .start()
	
	taskid[ip-1]. join()
	for i in range(0,256):
		if ip_exist[i] == 1:
			clientIp = "{0}.{1}.{2}.{3}".format(baseip[0],baseip[1],baseip[2],i)
	return clientIp

