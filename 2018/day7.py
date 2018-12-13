#! /usr/bin/env python3
import re

class Node:
	def __init__(self, name):
		self.name = name
		self.children = []
		self.parent = []

	def __str__(self):
		children = ", ".join(self.children)
		return "%s: %s" % (self.name, children)

	def __repr__(self):
		return self.__str__()

with open('input/day7') as input:
	lines = list(map(lambda x: x.strip(), input.readlines()))

pattern = 'Step\s(.).*step\s(.).*'
comp = re.compile(pattern)
deps = []
for line in lines:
	match = comp.match(line)
	deps.append((match.group(1), match.group(2)))


nodes = {}
for d in deps:
	p = d[0]
	c = d[1]
	pnode = nodes.get(p, None)
	cnode = nodes.get(c, None)
	if not pnode:
		pnode = Node(p)
		nodes[p] = pnode
	if not cnode:
		cnode = Node(c)
		nodes[c] = cnode
	pnode.children.append(c)
	cnode.parent.append(p)

vals = nodes.values()
result = ""
while len(vals) > 0:
	roots = []
	for n in vals:
		if not n.parent:
			roots.append(n)
	res = sorted(roots, key=lambda x: x.name)[0]
	result += res.name
	for c in res.children:
		nodes.get(c).parent.remove(res.name)
	del nodes[res.name]
	vals = nodes.values()

print("Part 1: %s" % result)


