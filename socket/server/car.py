#!/usr/bin/env python
#
#	car module
#
# todo: check error handle
#

import os
import sys
import os.path
import subprocess

__motorWheelRight = "/sys/class/motor/wheel-right/"
__motorWheelLeft = "/sys/class/motor/wheel-left/"
__motorPath = { "right":__motorWheelRight, "left":__motorWheelLeft }

#__ctlPath = __motorPath+"ctl"
#__statePath = __motorPath+"state"
#__speedPath = __motorPath+"speed"
__InsModule = "modprobe motor_l293d_dc"



def __IsDriverExist(path):
	if not os.path.exists(path):
		print "file {0} dont exist, try to probe motor.....".format(path)
		
		if subprocess.call(__InsModule.split()) != 0:
			print "Failed"
			return False
		print "succeeded"
	return True
	
def __GetWheelPath(wheel, type):
	if __motorPath.has_key(wheel):
		path = __motorPath[wheel] + type
	else:
		path = ""
	return path

def state(wheel):
	retdata = 'ERROR'
	statePath = __GetWheelPath(wheel, "state")
	if not __IsDriverExist(statePath):
		return retdata
	fd = open(statePath, 'r')
	if fd < 0:
		print "open error: motor r"
	else:
		retdata = fd.readline()
		print retdata
		fd.close()
	return retdata


def ctrl(wheel, step):
	retdata = 'ERROR'
	ctlPath = __GetWheelPath(wheel, "ctl")
	if not __IsDriverExist(ctlPath):
		return retdata
	fd = open(ctlPath, 'w');
	if fd < 0:
		print "open error: motor w "
	else:
		retdata = "{0}".format(step)+'\0'
		#print "{0} > motor".format(step)
		fd.write(retdata)
		fd.close()
		retdata = 'OK'
	return retdata


def setSpeed(wheel, pps):
	retdata = 'ERROR'
	speedPath = __GetWheelPath(wheel, "speed")
	if not __IsDriverExist(speedPath):
		return retdata
	fd = open(speedPath, 'r+');
	if fd < 0:
		print "open error: speed w "
	else:
		fd.write(pps)
		fd.close()
		retdata = 'OK'
	return retdata


def getSpeed(wheel):
	retdata = 'ERROR'
	speedPath = __GetWheelPath(wheel, "speed")
	if not __IsDriverExist(speedPath):
		return retdata
	fd = open(speedPath, 'r+');
	if fd < 0:
		print "open error: speed r "
	else:
		retdata = fd.readline()
		print retdata
		fd.close()

	return retdata



