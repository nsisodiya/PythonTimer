#!/usr/bin/python

#(c) 2011 , Narendra Sisodiya , narendra@narendrasisodiya.com 
#    Saturday, 09 April 2011

#
#   Released under MIT License
#

import time

class TickTockTimer:

	def StartTimer(self):
		self.TimerOffset = time.time()
		self.LastTicked = 0
		self.TimeWhenItWasPaused = 0
		self.paused = False
	
	def Tick(self):
		if self.paused == False:
			NewTicked = time.time() - self.TimerOffset
			diff = NewTicked - self.LastTicked
			self.LastTicked = NewTicked
			return diff
		else:
			print "Cannot Tick, Timer is paused"

	def GetTime(self):
		if self.paused == True:
			return self.TimeWhenItWasPaused
		else:
			return time.time() - self.TimerOffset
		
	def Pause(self):
		self.TimeWhenItWasPaused = time.time() - self.TimerOffset
		self.paused = True

	def UnPause(self):
		self.TimerOffset = time.time() - self.TimeWhenItWasPaused
		self.paused = False
	
	
'''
>>> import PythonTimer
>>> t = PythonTimer.TickTockTimer()
>>> t.StartTimer()
>>> t.GetTime()
3.9744668006896973

>>> t.GetTime()
4.7742757797241211
>>> t.GetTime()
5.4243037700653076
>>> t.GetTime()
15.794264793395996

>>> t.Pause()
>>> t.GetTime()
16.001962900161743
>>> t.GetTime()
16.001962900161743

>>> t.UnPause()
>>> t.GetTime()
18.171801805496216
>>> t.GetTime()
18.801760911941528
>>> t.GetTime()
19.371749877929688

'''

