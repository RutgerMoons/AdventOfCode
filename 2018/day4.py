#! /usr/bin/env python3
import re

class Action:
	def __init__(self, year, month, day, hour, minute, event):
		self.year = year
		self.month = month
		self.day = day
		self.hour = hour
		self.minute = minute
		self.event = event

	def setNumber(self, number):
		self.number = number

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return "[%d-%d-%d %d:%d]%s" % (self.year, self.month, self.day, self.hour, self.minute, self.event)

with open('input/test4') as input:
	vals = list(map(lambda x: x.strip(), input.readlines()))

actions = []
for val in vals:
	pattern = '\[(\d+)-(\d+)-(\d+)\s(\d+):(\d+)\](.*)'
	comp = re.compile(pattern)
	match = comp.match(val)
	print(match.group(0))
	year = int(match.group(1))
	month = int(match.group(2))
	day = int(match.group(3))
	hour = int(match.group(4))
	minute = int(match.group(5))
	event = match.group(6)
	actions.append(Action(year, month, day, hour, minute, event))

actions = sorted(actions, key=lambda x: (x.year, x.month, x.day, x.hour, x.minute))

#TODO: process actions
# Create an hours array per guard, increment minute entry per minute asleep
# find the max sleep and times that by the max minute
