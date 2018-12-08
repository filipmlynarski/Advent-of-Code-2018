import re

puzzle = open('puzzle', 'r').read().splitlines()
puzzle = [tuple(map(int, re.findall(r'\d+', i))) for i in puzzle]

alph = [chr(i) for i in range(ord('a'), ord('z')+1)]

def point_is_closest(x, y):
	distances = []
	for idx, point in enumerate(puzzle):
		distances.append((abs(point[0] - x) + abs(point[1] - y)))
	lowest = min(distances)
	if distances.count(lowest) == 1:
		return distances.index(lowest)+1
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

extend_grid = 200
shrink = extend_grid // 4

x1 -= extend_grid
y1 -= extend_grid
x2 += extend_grid
y2 += extend_grid

grid = {}

for x in range(x1, x2):
	for y in range(y1, y2):
		grid[(x, y)] = point_is_closest(x, y)

counted = []
for i in range(1, len(puzzle)+1):
	occurances = list(grid.values()).count(i)
	counted.append(occurances)

smaller_grid_values = [v for k, v in grid.items() if x1+shrink < k[0] < x2-shrink and y1+shrink < k[1] < y2-shrink]

counted2 = []
for i in range(1, len(puzzle)+1):
	occurances = smaller_grid_values.count(i)
	if occurances == counted[i-1]:
		counted2.append(occurances)
	else:
		counted2.append(0)

highest_area = sorted(counted2)[-1]
print(highest_area)