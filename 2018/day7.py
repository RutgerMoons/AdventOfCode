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

# part 2
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

time_offset = 60
workers = 5
tasks = []

total_time = 0
vals = nodes.values()
while len(vals) > 0:
	roots = []
	task_names = list(map(lambda x: x[0], tasks))
	for n in vals:
		if not n.parent and not n.name in task_names:
			roots.append(n)
	sorted_roots = sorted(roots, key=lambda x: x.name)
	available_spots = workers - len(tasks)
	for i in range(min(len(sorted_roots), available_spots)):
		task_node = sorted_roots[i]
		tasks.append((task_node.name, time_offset + ord(task_node.name) - ord('A') + 1))


	vals = nodes.values()

	min_time = min(list(map(lambda x: x[1], tasks)))
	total_time += min_time
	for t in range(len(tasks)):
		tasks[t] = (tasks[t][0], tasks[t][1] - min_time)
	for t in tasks:
		if t[1] == 0:
			tasks.remove(t)
			task_node = nodes.get(t[0])
			for c in task_node.children:
				nodes.get(c).parent.remove(task_node.name)
			del nodes[task_node.name]


print("Part 1: %d" % total_time)
