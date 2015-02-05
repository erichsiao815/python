#!/usr/bin/env python
#

import os
import sys
import time
import evdev
from threading import Thread

class dirkey(object):
	def __init__(self):
		kbd = "/dev/input/event2"	#TBD!! to fix it, donot be a constant
		self.key_up = False
		self.key_down = False
		self.key_right = False
		self.key_left = False
		self.key_leave = False
		self.taskfd = -1

	def recive_event(self):
		dev = evdev.InputDevice("/dev/input/event2")
		print dev
		while True:
			for event in dev.read_loop():
				if event.type == evdev.ecodes.EV_KEY and event.code == evdev.ecodes.KEY_UP:
					if event.value == 0:	#up
						print "KEY_UP clr"
						self.key_up = False
					elif event.value == 1:	#down
						print "KEY_UP set"
						self.key_up = True
				elif event.type == evdev.ecodes.EV_KEY and event.code == evdev.ecodes.KEY_DOWN:
					if event.value == 0:	#up
						print "KEY_DOWN clr"
						self.key_down = False
					elif event.value == 1:	#down
						print "KEY_DOWN set"
						self.key_down = True
				elif event.type == evdev.ecodes.EV_KEY and event.code == evdev.ecodes.KEY_RIGHT:
					if event.value == 0:	#up
						print "KEY_RIGHT clr"
						self.key_right = False
					elif event.value == 1:	#down
						print "KEY_RIGHT set"
						self.key_right = True
				elif event.type == evdev.ecodes.EV_KEY and event.code == evdev.ecodes.KEY_LEFT:
					if event.value == 0:	#up
						print "KEY_LEFT clr"
						self.key_left = False
					elif event.value == 1:	#down
						print "KEY_LEFT set"
						self.key_left = True
				elif event.type == evdev.ecodes.EV_KEY and event.code == evdev.ecodes.KEY_Q:
					if event.value == 0:	#up
						print "press q to leave....."
						self.key_leave = True
						time.sleep(1)
						return
					

	#def start():
		#taskfd = Thread(target=recive_event)
		#taskfd.start()
		
		
		
	#def exit():
		#taskfd.exit()
		#print "leave"
		
		








