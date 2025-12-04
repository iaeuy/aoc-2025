banks = []
with open("input") as f:
	for line in f:
		banks.append([int(n) for n in line.rstrip()])

def bank_joltage_naive(bank):
	result = 11
	for i in range(len(bank)):
		for j in range(i):
			result = max(result, 10 * bank[j] + bank[i])
	return result

def bank_joltage_linear(bank):
	result = 11
	max_start = 0
	for num in bank:
		result = max(result, max_start * 10 + num) 
		max_start = max(max_start, num)
	return result

def part_1_naive(banks):
	return sum(map(bank_joltage_naive, banks))
print(part_1_naive(banks))

def part_1_linear(banks):
	return sum(map(bank_joltage_linear, banks))
print(part_1_linear(banks))
