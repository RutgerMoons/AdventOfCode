#! /usr/bin/env python3


with open('input/day8') as input:
	lines = input.readlines()
	values = list(map(int, lines[0].strip().split(" ")))


class Node:
	def __init__(self):
		self.children = []
		self.metadata = []

	def __repr__(self):
		result = "Metadata: [%s]" % ", ".join(map(str, self.metadata))
		return result

	def node_sum(self):
		if not self.children:
			return sum(self.metadata)

		total = 0
		for i in self.metadata:
			idx = i - 1
			if idx < 0 or idx >= len(self.children):
				continue
			total += self.children[idx].node_sum()
		return total

def parseValue(values):
	idx, root = _parseValue(values, 0)
	return root

def _parseValue(values, idx):
	nbChildren = values[idx]
	nbMetadata = values[idx + 1]
	idx += 2

	current = Node()

	for i in range(nbChildren):
		new_idx, child = _parseValue(values, idx)
		current.children.append(child)
		idx = new_idx

	current.metadata = values[idx:idx + nbMetadata]
	return idx + nbMetadata, current

def sum_metadata(node):
	return _sum_metadata(node, 0)

def _sum_metadata(node, count):
	if not node.children:
		return count + sum(node.metadata)

	total = 0
	for c in node.children:
		total += _sum_metadata(c, 0)
	return total + sum(node.metadata)
	

root = parseValue(values)
total_metadata = sum_metadata(root)


print("Part 1: %s" % total_metadata)

print("Part 2: %s" % root.node_sum())
