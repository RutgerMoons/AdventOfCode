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

serial = 18
grid_size = 3
board_size = 300
board = []
for i in range(board_size):
	board.append([0] * board_size)

for x in range(board_size):
	for y in range(board_size):
		board[x][y] = calc_power_cell(x + 1, y + 1, serial)

top_x, top_y, max_power = calc_total_power(board, grid_size)
print("Top coordinate: {}, {} with power {}".format(top_x, top_y, max_power))
