from collections import Counter

def part_1():
	splits = 0
	beam_indices = set()
	with open("input") as f:
		beam_indices.add(f.readline().find('S'))
		for line in f:
			new_beam_indices = set()
			for i, char in enumerate(line):
				if not i in beam_indices:
					continue
				if char == '^':
					splits += 1
					new_beam_indices.add(i - 1)
					new_beam_indices.add(i + 1)
				else:
					new_beam_indices.add(i)
			beam_indices = new_beam_indices
	return splits
print(part_1())

def part_2():
	with open("input") as f:
		manifold = f.readlines()

	counts = Counter()
	for i in range(len(manifold[-1])):
		counts[(i, len(manifold) - 1)] = 1

	start = (manifold[0].find('S'), 0)
	stack = [(manifold[0].find('S'), 0, [])]
	while stack:	
		beam_index, row, path = stack.pop()
		node = (beam_index, row)
		if node in counts:
			for prev_node in path:
				counts[prev_node] += counts[node]
		else:
			new_path = list(path)
			new_path.append(node)
			if manifold[row + 1][beam_index] == '^':
				stack.append((beam_index - 1, row + 1, new_path))
				stack.append((beam_index + 1, row + 1, new_path))
			else:
				stack.append((beam_index, row + 1, new_path))
	return counts[start]
print(part_2())
