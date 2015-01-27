#!/usr/bin/env python

import os
import sys
import os.path

motorPath = "/sys/class/motor/motor"

def state():
	retdata = 'ERROR'
	if os.path.exists(motorPath) :
		fd = open(motorPath, 'r+')
		if fd < 0:
			print "error: motor r  open"
		else:
			retdata = fd.readline()
			print retdata
			fd.close()
	else:
		print "file dont exist"
	return retdata


def ctrl(step):
	retdata = 'ERROR'
	if os.path.exists(motorPath):
		fd = open(motorPath, 'r+');
		if fd < 0:
			print "error: motor w open"
		else:
			retdata = "{0}".format(step)+'\0'
			print "{0} > motor\n".format(step)
			fd.write(retdata)
			fd.close()
			retdata = 'OK'
	else:
		print "file dont exist"
	return retdata

