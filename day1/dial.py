moves = []
with open("input") as f:
	for line in f:
		direction = 1 if line[0] == 'R' else -1
		length = int(line[1:])
		moves.append((direction, length))

def part_1():
	position = 50
	password = 0
	for (direction, length) in moves:
		position += direction * length
		position %= 100
		if not position:
			password += 1
	print(password)
part_1()

def part_2():
	position = 50
	password = 0
	for (direction, length) in moves:
		old_pos = position
		position += direction * length

		clicks = 0
		if position <= 0:
			clicks += -1 * position // 100 + 1
			if not old_pos:
				clicks -= 1
		else:
			clicks += position // 100

		password += clicks
		position %= 100
	print(password)
part_2()
