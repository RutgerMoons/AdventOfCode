#! /usr/bin/env python3
import re

class Star:
	def __init__(self, pos, vel):
		self.x, self.y = pos
		self.vel_x, self.vel_y = vel

	def __repr__(self):
		return "({}, {}) -> ({}, {})".format(self.x, self.y, self.vel_x, self.vel_y)

def get_max_dimensions(stars):
	min_x = 100
	max_x = -100
	min_y = 100
	max_y = -100

	for star in stars:
		if star.x < min_x: min_x = star.x
		if star.x > max_x: max_x = star.x
		if star.y < min_y: min_y = star.y
		if star.y > max_y: max_y = star.y
	return min_x, max_x, min_y, max_y

def print_stars(stars, counter):
	min_x, max_x, min_y, max_y = get_max_dimensions(stars)
	if min_x < 0 or min_y < 0:
		return False
	
	board = []
	for i in range(max_y + 1):
		t = "." * (max_x + 1 - min_x)
		board.append(t)
	
	for star in stars:
		x = star.x - min_x
		line = board[star.y]
		board[star.y] = line[:x] + '#' + line[x + 1:]
	
	print("\n\n{}".format(counter))
	for line in board:
		if '#' not in line: continue
		print(line)

	return True

def simulate_stars(stars):
	for star in stars:
		star.x += star.vel_x
		star.y += star.vel_y


with open('input/test10') as input:
	lines = list(map(lambda x: x.strip(), input.readlines()))

pattern = '.*<\s*(.+)\s*>.*<\s*(.+)\s*>.*'
comp = re.compile(pattern)
stars = []
for line in lines:
	match = comp.match(line)
	pos_str = tuple(match.group(1).split(","))
	pos = (int(pos_str[0].strip()), int(pos_str[1].strip()))
	vel_str = tuple(match.group(2).split(","))
	vel = (int(vel_str[0].strip()), int(vel_str[1].strip()))
	stars.append(Star(pos, vel))

for i in range(100000):
	print_stars(stars, i)
	simulate_stars(stars)
