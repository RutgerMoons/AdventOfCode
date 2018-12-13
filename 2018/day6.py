#! /usr/bin/env python3

with open('input/day6') as input:
	coords = list(map(lambda x: (int(x.split(", ")[0]), int(x.split(", ")[1])), input.readlines()))

max_x = max(map(lambda x : x[0], coords))
max_y = max(map(lambda x : x[1], coords))


board_width = 3 * max_x
board_height = 3 * max_y
board = []
# cell:
# fst -> id (-1 -> means owned by none)
# sec -> distance
for i in range(board_width):
	t = []
	for j in range(board_height):
		t.append((-1, -1))
	board.append(t)

for idx, c in enumerate(coords):
	x, y = c
	x += max_x
	y += max_y
	for i in range(board_width):
		dist_x = abs(x - i)
		for j in range(board_height):
			dist_y = abs(y - j)
			distance = dist_x + dist_y

			cell = board[i][j]
			if cell[1] > distance or cell[1] == -1:
				board[i][j] = (idx, distance)
			elif cell[1] == distance:
				board[i][j] = (-1, distance)

def count_node(board, id):
	total = 0
	for i in range(board_width):
		for j in range(board_height):
			total += board[i][j][0] == id
	return total

# every coord on the edge should be removed:
def remove_edge_coords(board, coords):
	bad = set()
	good = list(range(len(coords)))
	for i in range(board_width):
		for j in [0, board_height - 1]:
			id = board[i][j][0]
			if id > -1:
				bad.add(id)
	for j in range(board_height):
		for i in [0, board_width - 1]:
			id = board[i][j][0]
			if id > -1:
				bad.add(id)
	for i in bad:
		good.remove(i)
	return good

m = -1
candidates = remove_edge_coords(board, coords)
for cand in candidates:
	area = count_node(board, cand)
	if area > m:
		m = area

print("Part 1: %d" % m)
