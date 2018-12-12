#! /usr/bin/env python3
import re

with open('input/day5') as input:
	polymer = list(map(lambda x: x.strip(), input.readlines()))[0]

def react(polymer):
	found = True
	while found:
		found = False
		for i in range(len(polymer) - 1):
			c1, c2 = polymer[i], polymer[i + 1]
			
			if c1.upper() == c2.upper() and \
				(c1.isupper() and c2.islower() or \
				 c1.islower() and c2.isupper()):
				found = True
				polymer = polymer.replace(c1+c2, '')
				polymer = polymer.replace(c2+c1, '')
				break
	return polymer

x = polymer
x = react(x)

print("Part 1: %d" % len(x))

shortest = len(polymer)

begin = ord('a')
for i in range(26):
	x = polymer

	lower, upper = chr(begin + i), chr(begin + i).upper()
	removed = x.replace(lower, '')
	removed = removed.replace(upper, '')
	reacted = react(removed)
	length = len(reacted)
	print("%s/%s: %d" % (lower, upper, length))
	if length < shortest:
		shortest = length

print("Part 2: %d" % shortest)
