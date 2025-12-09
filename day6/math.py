from functools import reduce

numbers = []
ops = []
with open("input") as f:
	for line in f:
		parsed = line.rstrip().split()
		if parsed[0] == '*' or parsed[0] == '+':
			ops = parsed
		else:
			numbers.append(parsed)

def get_reducer(op):
	if op == '*':
		return lambda x, y: x * y
	else:
		return lambda x, y: x + y

def part_1(numbers, ops):
	result = 0
	for i in range(len(ops)):
		result += reduce(get_reducer(ops[i]), [int(row[i]) for row in numbers])
	return result
print(part_1(numbers, ops))

def get_cephalopod_problems():
	"""Returns number array problems, sans operations"""
	with open("input") as f:
		raw_nums = [line.rstrip("\n") for line in f.readlines()[:-1]]
	width = len(raw_nums[0])
	height = len(raw_nums)

	problems = []
	curr_prob = []
	for i in range(width):
		num = " ".join([raw_nums[j][-1-i] for j in range(height)])
		spaces_removed = num.replace(" ", "")
		if spaces_removed:
			curr_prob.append(int(spaces_removed))
		else:
			problems.append(curr_prob)
			curr_prob = []
	if curr_prob:
		problems.append(curr_prob)

	return problems

def part_2(problems, ops):
	result = 0
	for i in range(len(ops)):
		result += reduce(get_reducer(ops[-1-i]), problems[i])
	return result
print(part_2(get_cephalopod_problems(), ops))
