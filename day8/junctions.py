import math
import heapq

boxes = []
with open("input") as f:
	for line in f:
		boxes.append(tuple(int(n) for n in line.rstrip().split(',')))

box_pairs = []
distances = {}
for i in range(len(boxes)):
	for j in range(i - 1):
		box1, box2 = boxes[i], boxes[j]
		distances[(box1, box2)] = math.dist(box1, box2)
		box_pairs.append((box1, box2))
box_pairs.sort(key=lambda pair: distances[pair])

def connect_boxes(circuits, box1, box2):
	for circuit in circuits:
		if box1 in circuit:
			box1_circuit = circuit
		if box2 in circuit:
			box2_circuit = circuit
	if box1_circuit != box2_circuit:
		circuits.remove(box1_circuit)
		circuits.remove(box2_circuit)
		circuits.add(box1_circuit | box2_circuit)

def part_1():
	circuits = set(frozenset({box}) for box in boxes)
	for i in range(1000):
		box1, box2 = box_pairs[i]
		connect_boxes(circuits, box1, box2)
	return math.prod(heapq.nlargest(3, map(len, circuits)))
print(part_1())

def part_2():
	circuits = set(frozenset({box}) for box in boxes)
	for i in range(len(box_pairs)):
		box1, box2 = box_pairs[i]
		connect_boxes(circuits, box1, box2)
		if len(circuits) == 1:
			return box1[0] * box2[0]
print(part_2())
