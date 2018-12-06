import re
from collections import defaultdict

puzzle = open('puzzle', 'r').read().splitlines()
puzzle = [tuple(map(int, re.findall(r'\d+', i))) for i in puzzle]

def is_close_enough(x, y):
	distances = 0
	for point in puzzle:
		distances += abs(point[0] - x) + abs(point[1] - y)
	if distances < 10000:
		return 1
	return 0

x1, x2, y1, y2 = puzzle[0][0], puzzle[0][0], puzzle[0][1], puzzle[0][1]

for i in puzzle:
	if i[0] < x1:
		x1 = i[0]
	if i[0] > x1:
		x2 = i[0]
	if i[1] < x1:
		y1 = i[1]
	if i[1] > x1:
		y2 = i[1]

x1 -= 10000 // len(puzzle) - 1
y1 -= 10000 // len(puzzle) - 1
x2 += 10000 // len(puzzle) + 1
y2 += 10000 // len(puzzle) + 1

grid = {}
close_enough = 0

for x in range(x1, x2):
	for y in range(y1, y2):
		close_enough += is_close_enough(x, y)

print(close_enough)