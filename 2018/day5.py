#! /usr/bin/env python3
import re

with open('input/day5') as input:
	polymer = list(map(lambda x: x.strip(), input.readlines()))[0]

found = True
while found:
	print(len(polymer))
	found = False
	for i in range(len(polymer) - 1):
		c1, c2 = polymer[i], polymer[i + 1]
		
		if c1.upper() == c2.upper() and \
			(c1.isupper() and c2.islower() or \
			 c1.islower() and c2.isupper()):
			found = True
			polymer = polymer[:i] + polymer[i+2:]
			break

print("Part 1: %d" % len(polymer))

