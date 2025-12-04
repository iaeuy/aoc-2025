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

def part_2_joltage_recursive(bank, k, memo):
	bank = tuple(bank)
	if (bank, k) in memo:
		return memo[(bank, k)]
	elif k == 1:
		result = max(bank)
	elif len(bank) == k:
		result = int("".join(map(str, bank)))
	else:
		result = max(
			part_2_joltage_recursive(bank[1:], k, memo),
			int(str(bank[0]) + str(part_2_joltage_recursive(bank[1:], k - 1, memo)))
		)
	memo[(bank, k)] = result
	return result

def part_2_recursive(banks):
	memo = {}
	return sum(map(lambda bank: part_2_joltage_recursive(bank, 12, memo), banks))
print(part_2_recursive(banks))