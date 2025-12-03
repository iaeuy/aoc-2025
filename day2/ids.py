def parse_input(id_ranges):
	ranges = []
	for id_range in id_ranges.split(","):
		lower, upper = id_range.split("-")
		ranges.append((int(lower), int(upper)))
	return ranges

with open("input") as f:
	ranges = parse_input(f.readline())

def sum_adj(start, end):
	"""Return the sum start + (start + 1) + ... + end"""
	return (start + end) * (end - start + 1) // 2

def sum_2_invalid_fixed_digits(start, end, digits):
	"""Given start and end that are both digits long, return the sum of
	all 2-invalid numbers between start and end"""
	if digits % 2 == 1:
		return 0

	digit_shift = 10 ** (digits // 2)

	# Get smallest invalid >= start
	start_first_half = start // digit_shift
	start_second_half = start % digit_shift
	if start_first_half < start_second_half:
		invalid_start = start_first_half + 1
	else:
		invalid_start = start_first_half

	# Get largest invalid <= end
	end_first_half = end // digit_shift
	end_second_half = end % digit_shift
	if end_first_half > end_second_half:
		invalid_end = end_first_half - 1
	else:
		invalid_end = end_first_half

	if invalid_start > invalid_end:
		return 0

	return sum_adj(invalid_start, invalid_end) * (digit_shift + 1)

def sum_2_invalid(start, end):
	"""Return the sum of 2-invalid numbers between start and end"""
	result = 0
	curr_start = start
	while curr_start <= end:
		curr_digits = len(str(curr_start))
		if curr_digits == len(str(end)):
			curr_end = end
		else:
			curr_end = 10 ** curr_digits - 1
		result += sum_2_invalid_fixed_digits(curr_start, curr_end, curr_digits)
		curr_start = curr_end + 1
	return result

def part_1():
	return sum([sum_2_invalid(start, end) for (start, end) in ranges])
print(part_1())

def is_k_invalid(n, k):
	"""Return whether n is a number concatenated k times"""
	digits = len(str(n))
	if digits % k != 0:
		return False
	return n == int(str(n)[:(digits // k)] * k)

def is_invalid(n):
	digits = len(str(n))
	return any([is_k_invalid(n, k) for k in range(2, digits + 1)])

def sum_invalid(start, end):
	return sum([n for n in range(start, end + 1) if is_invalid(n)])

def part_2():
	return sum([sum_invalid(start, end) for (start, end) in ranges])
print(part_2())
