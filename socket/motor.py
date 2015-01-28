#!/usr/bin/env python
#
#	motor's module
#
# todo: check error handle
#

import os
import sys
import os.path
import subprocess

__motorPath = "/sys/class/motor/motor"
__ppsPath = "/sys/class/motor/hz"
__InsModule = "modprobe motor_28byj_48"


def __IsDriverExist(path):
	if not os.path.exists(path):
		print "file dont exist, try to probe motor....."
		
		if subprocess.call(__InsModule.split()) != 0:
			print "Failed"
			return False
		print "succeeded"
	return True
	
	
def state():
	retdata = 'ERROR'
	if not __IsDriverExist(__motorPath):
		return retdata
	fd = open(__motorPath, 'r+')
	if fd < 0:
		print "open error: motor r"
	else:
		retdata = fd.readline()
		print retdata
		fd.close()
	return retdata


def ctrl(step):
	retdata = 'ERROR'
	if not __IsDriverExist(__motorPath):
		return retdata
	fd = open(__motorPath, 'r+');
	if fd < 0:
		print "open error: motor w "
	else:
		retdata = "{0}".format(step)+'\0'
		print "{0} > motor\n".format(step)
		fd.write(retdata)
		fd.close()
		retdata = 'OK'
	return retdata


def setSpeed(pps):
	retdata = 'ERROR'
	if not __IsDriverExist(__ppsPath):
		return pps
	fd = open(__ppsPath, 'r+');
	if fd < 0:
		print "open error: speed w "
	else:
		fd.write(pps)
		fd.close()
		retdata = 'OK'
	return retdata


def getSpeed():
	pps = 'ERROR'
	if not __IsDriverExist(__ppsPath):
		return pps
	fd = open(__ppsPath, 'r+');
	if fd < 0:
		print "open error: speed r "
	else:
		pps = fd.readline()
		print pps
		fd.close()

	return pps



