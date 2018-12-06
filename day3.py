#! /usr/bin/env python3

class Rectangle:
	def __init__(self, offset, dimensions):
		self.left = offset[0]
		self.up = offset[1]
		self.width = dimensions[0]
		self.height = dimensions[1]

with open('input/day3') as input:
	vals = list(map(lambda x: x.strip(), input.readlines()))



# parse the lines
rectangles = []
for val in vals:
	split = val.split()
	offset = tuple(map(int, split[2].strip()[:-1].split(',')))
	dimensions = tuple(map(int, split[3].strip().split('x')))
	rectangles.append(Rectangle(offset, dimensions))

board_width, board_height = 0, 0
for r in rectangles:
	board_width = max(board_width, r.left + r.width)
	board_height = max(board_height, r.up + r.height)

board = []
for i in range(board_height):
	board.append([0] * board_width)

for r in rectangles:
	for i in range(r.height):
		y = r.up + i
		for j in range(r.width):
			x = r.left + j
			board[y][x] += 1

total = 0
for i in range(board_height):
	for j in range(board_width):
		total += board[i][j] > 1

print(total)
