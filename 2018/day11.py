#! /usr/bin/env python3

def calc_power_cell(x, y, serial):
	rack_id = x + 10
	power = rack_id * y
	power += serial
	power *= rack_id
	power //= 100
	power %= 10
	power -= 5
	return power

def calc_total_power(board, grid_size):
	top_x, top_y = 1,1
	max_power = -100

	for x in range(len(board[0]) - grid_size + 1):
		for y in range(len(board) - grid_size + 1):
			power = 0
			for i in range(grid_size):
				for j in range(grid_size):
					power += board[x + i][y + j]
			if power > max_power:
				max_power = power
				top_x, top_y = x + 1, y + 1
	return top_x, top_y, max_power

def calc_dynamic(board, x, y, g, sums):
	bad_val = None
	get = sums.get((x,y,g), bad_val)
	if get != bad_val:
		return get
	
	if g == 1:
		val = board[x][y]
		sums[(x,y,1)] = val
		return val
	
	val = calc_dynamic(board, x + 1, y + 1, g - 1, sums) + sum(board[x][y:y+g])
	for i in range(1, g):
		val += board[x+i][y]
	sums[(x, y, g)] = val
	return val

def calc_all_sums(board):
	sums = {}
	for g in range(1, len(board) + 1):
		print("g: {}".format(g))
		for x in range(len(board) + 1 - g):
			for y in range(len(board) + 1 - g):
				calc_dynamic(board, x, y, g, sums)
	return sums

def calc_total_power_variable_grid_size(board):
	top_x, top_y = 1, 1
	max_power = -100
	max_grid = 1
	sums = calc_all_sums(board)

	for g in range(1, len(board) + 1):
		for x in range(len(board)):
			for y in range(len(board)):
				p = sums.get((x, y, g), None)
				if p == None:
					continue
				if p > max_power:
					max_power = p
					top_x, top_y = x + 1, y + 1
					max_grid = g
	return top_x, top_y, max_grid, max_power

serial = 6303
board_size = 300
board = []
for i in range(board_size):
	board.append([0] * board_size)

for x in range(board_size):
	for y in range(board_size):
		board[x][y] = calc_power_cell(x + 1, y + 1, serial)


top_x, top_y, max_power = calc_total_power(board, 3)
print("Part 1: Top coordinate: {}, {} with power {}".format(top_x, top_y, max_power))

top_x, top_y, max_grid, max_power = calc_total_power_variable_grid_size(board)
print("Part 2: Top coordinate: {}, {} with power {}, for grid size {}".format(top_x, top_y, max_power, max_grid))
