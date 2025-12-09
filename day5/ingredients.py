fresh_ranges = []
ids = []
with open("input") as f:
    reading_ranges = True
    for line in f:
        line = line.strip()
        if line == "":
            reading_ranges = False
            continue
        if reading_ranges:
            lower, upper = line.split('-')
            fresh_ranges.append([int(lower), int(upper)])
        else:
            ids.append(int(line))

def sort_and_merge(fresh_ranges):
    result = []
    for r in sorted(fresh_ranges):
        if not result:
            result.append(r)
            continue
        curr_range = result[-1]
        if r[0] <= curr_range[1]:
            curr_range[1] = max(curr_range[1], r[1])
        else:
            result.append(r)
    return result

def search_ranges(fresh_ranges, n):
    if n < fresh_ranges[0][0] or n > fresh_ranges[-1][1]:
        return False
    lower = 0
    upper = len(fresh_ranges) - 1
    while lower <= upper:
        i = (lower + upper) // 2
        curr_range = fresh_ranges[(lower + upper) // 2]
        if n >= curr_range[0] and n <= curr_range[1]:
            return True
        if n < curr_range[0]:
            upper = i - 1
        else:
            lower = i + 1 
    return False

def part_1(fresh_ranges, ids):
    merged = sort_and_merge(fresh_ranges)
    return len([n for n in ids if search_ranges(merged, n)])
print(part_1(fresh_ranges, ids))

def part_2(fresh_ranges):
    merged = sort_and_merge(fresh_ranges)
    return sum(r[1] - r[0] + 1 for r in merged)
print(part_2(fresh_ranges))
