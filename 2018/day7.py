#! /usr/bin/env python3
import re

with open('input/test7') as input:
	lines = list(map(lambda x: x.strip(), input.readlines()))

pattern = 'Step\s(.).*step\s(.).*'
comp = re.compile(pattern)
deps = []
for line in lines:
	match = comp.match(line)
	deps.append((match.group(1), match.group(2)))

print(deps)

