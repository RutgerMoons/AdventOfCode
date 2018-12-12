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

class Guard:
	def __init__(self, number):
		self.minutes = [0] * 60
		self.start_sleep = None
		self.number = number

	def total_sleep(self):
		return sum(self.minutes)

	def max_minute(self):
		idx, val = -1, -1
		for i in range(len(self.minutes)):
			if self.minutes[i] > val:
				idx = i
				val = self.minutes[i]
		return idx, val

with open('input/day4') as input:
	vals = list(map(lambda x: x.strip(), input.readlines()))

actions = []
for val in vals:
	pattern = '\[(\d+)-(\d+)-(\d+)\s(\d+):(\d+)\](.*)'
	comp = re.compile(pattern)
	match = comp.match(val)
	year = int(match.group(1))
	month = int(match.group(2))
	day = int(match.group(3))
	hour = int(match.group(4))
	minute = int(match.group(5))
	event = match.group(6)
	actions.append(Action(year, month, day, hour, minute, event))

actions = sorted(actions, key=lambda x: (x.year, x.month, x.day, x.hour, x.minute))

guards = {}
current_guard = -1

pattern = '.*#(\d+).*'
compilation = re.compile(pattern)
for ac in actions:
	if '#' in ac.event:
		match = compilation.match(ac.event)
		number = int(match.group(1))
		current_guard = number
		if guards.get(current_guard, None) is None:
			guards[current_guard] = Guard(current_guard)
	else:
		if 'sleep' in ac.event:
			guards.get(current_guard).start_sleep = ac.minute
		else:
			g = guards.get(current_guard)
			start_sleep = g.start_sleep
			end_sleep = ac.minute

			for i in range(end_sleep - start_sleep):
				g.minutes[i + start_sleep] += 1

max_guard = None
max_sleep = -1
for guard in guards.values():
	if guard.total_sleep() > max_sleep:
		max_sleep = guard.total_sleep()
		max_guard = guard

print("Part 1: guard number: %d, max minute: %d, answer: %d" % (max_guard.number, max_guard.max_minute()[0], max_guard.number * max_guard.max_minute()[0]))

max_guard = None
max_minute_count = -1
max_minute_idx = -1
for guard in guards.values():
	max_minute, val = guard.max_minute()
	if val > max_minute_count:
		max_guard = guard
		max_minute_count = val
		max_minute_idx = max_minute

print("Part 2: guard number: %d, max minute: %d, answer: %d" % (max_guard.number, max_minute_idx, max_guard.number * max_minute_idx))
