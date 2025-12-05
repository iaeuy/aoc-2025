grid = []
with open("input") as f:
	grid = [line.strip() for line in f]

def count_adj(grid, i, j):
	count = 0
	to_check_i = [n for n in [i - 1, i, i + 1] if n >= 0 and n < len(grid)]
	to_check_j = [m for m in [j - 1, j, j + 1] if m >= 0 and m < len(grid[0])]
	for n in to_check_i:
		for m in to_check_j:
			if (n, m) == (i, j):
				continue
			if grid[n][m] == '@':
				count += 1
	return count

def part_1(grid):
	accessible = 0
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == '@' and count_adj(grid, i, j) < 4:
				accessible += 1
	return accessible
print(part_1(grid))

def part_2(grid):
	removed = 0
	cycle = 0
	while True:
		prev_removed = removed
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				if grid[i][j] == '@' and count_adj(grid, i, j) < 4:
					removed += 1
					grid[i] = grid[i][:j] + '.' + grid[i][j + 1:] 
		cycle += 1
		if prev_removed == removed:
			break
	return removed
print(part_2(grid))