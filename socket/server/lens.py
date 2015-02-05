#!/usr/bin/env python
#
#	lens module
#
# todo: check error handle
#

import os
import sys
import os.path
import subprocess
import time


__motorZoom = "/sys/class/motor/zoom/"
__motorFocus = "/sys/class/motor/stepper/"
__motorPath = { "zoom":__motorZoom, "focus":__motorFocus }

__InsModule = "modprobe motor_l293d_cas292"



def __IsDriverExist(path):
	if not os.path.exists(path):
		print "file {0} dont exist, try to probe motor.....".format(path)
		
		if subprocess.call(__InsModule.split()) != 0:
			print "Failed"
			return False
		print "succeeded"
	return True
	
def __GetLensPath(motor, type):
	if __motorPath.has_key(motor):
		path = __motorPath[motor] + type
	else:
		path = ""
	return path

def state(motor):
	retdata = 'ERROR'
	statePath = __GetLensPath(motor, "state")
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


def ctrl(motor, step):
	retdata = 'ERROR'
	ctlPath = __GetLensPath(motor, "ctl")
	if not __IsDriverExist(ctlPath):
		return retdata
	fd = open(ctlPath, 'w');
	if fd < 0:
		print "open error: motor w "
	else:
		retdata = "{0}".format(step)+'\0'
		print "{0} > ".format(step),motor
		fd.write(retdata)
		fd.close()
		retdata = 'OK'
	return retdata


def setSpeed(motor, pps):
	retdata = 'ERROR'
	speedPath = __GetLensPath(motor, "speed")
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


def getSpeed(motor):
	retdata = 'ERROR'
	speedPath = __GetLensPath(motor, "speed")
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

def setPos(motor, pos):
	retdata = 'ERROR'
	posPath = __GetLensPath(motor, "pos")
	if not __IsDriverExist(posPath):
		return retdata
	fd = open(posPath, 'r+');
	if fd < 0:
		print "open error: speed w "
	else:
		fd.write(pos)
		fd.close()
		retdata = 'OK'
	return retdata


def getPos(motor):
	print motor
	retdata = 'ERROR'
	posPath = __GetLensPath(motor, "pos")
	print posPath
	if not __IsDriverExist(posPath):
		return retdata
	fd = open(posPath, 'r');
	if fd < 0:
		print "open error: speed r "
	else:
		retdata = fd.read()
		print retdata
		fd.close()
	return retdata




