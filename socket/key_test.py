#!/usr/bin/env python
#

import os
import sys
import time
import evdev


kbd = "/dev/input/event2"	#TBD!! to fix it, donot be a constant
key_up = False
key_down = False
key_right = False
key_left = False

def recive_event()
	dev = evdev.InputDevice(kbd)
	print dev
	while True:
		for event in dev.read_loop():
			if event.type == evdev.ecodes.EV_KEY and event.code == evdev.ecodes.KEY_UP:
				if event.value == 0:	#up
					print "KEY_UP clr"
					key_up = False
				elif event.value == 1:	#down
					print "KEY_UP set"
					key_up = True
			elif event.type == evdev.ecodes.EV_KEY and event.code == evdev.ecodes.KEY_DOWN:
				if event.value == 0:	#up
					print "KEY_DOWN clr"
					key_down = False
				elif event.value == 1:	#down
					print "KEY_DOWN set"
					key_up = True
			elif event.type == evdev.ecodes.EV_KEY and event.code == evdev.ecodes.KEY_RIGHT:
				if event.value == 0:	#up
					print "KEY_RIGHT clr"
					key_right = False
				elif event.value == 1:	#down
					print "KEY_RIGHT set"
					key_right = True
			elif event.type == evdev.ecodes.EV_KEY and event.code == evdev.ecodes.KEY_LEFT:
				if event.value == 0:	#up
					print "KEY_LEFT clr"
					key_left = False
				elif event.value == 1:	#down
					print "KEY_LEFT set"
					key_left = True








