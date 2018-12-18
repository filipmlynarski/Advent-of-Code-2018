import re
from collections import defaultdict

puzzle = open('puzzle', 'r').read().splitlines()
#puzzle = [list(map(int, re.findall(r'-?\d+', i))) for i in puzzle]

def print_ground():
	#maximum = 100
	for y in range(0, maximum+1):
		for x in range(400, 600):
			print(ground[(y, x)], end='')
		print()

ground = defaultdict(lambda: '.')
ground[(0, 500)] = '+'

minimum = 1e10
maximum = -1

for line in puzzle:
	converted = {i[0]: i.split('=')[-1] for i in line.split(', ')}
	if '..' in converted['x']:
		x = list(map(int, converted['x'].split('..')))
		y = [int(converted['y'])] * 2
	else:
		y = list(map(int, converted['y'].split('..')))
		x = [int(converted['x'])] * 2

	if y[1] > maximum:
		maximum = y[1]
	if y[0] < minimum:
		minimum = y[0]

	x[1] += 1
	y[1] += 1

	for y_idx in range(*y):
		for x_idx in range(*x):
			ground[(y_idx, x_idx)] = '#'


def fill(cords):
	left, right = list(cords), list(cords)
	leak = []

	while ground[tuple(left)] != '#':
		if ground[(left[0]+1, left[1])] == '.':
			leak.append(tuple(left))
			break

		ground[tuple(left)] = '~'
		left[1] -= 1
		
	while ground[tuple(right)] != '#':
		if ground[(right[0]+1, right[1])] == '.':
			leak.append(tuple(right))
			break

		ground[tuple(right)] = '~'
		right[1] += 1

	return leak
		

def drop(cords):
	while ground[cords] != '#':
		ground[cords] = '|'
		cords = (list(cords)[0] + 1, cords[1])

		if cords[0] > maximum:
			return

	cords = (list(cords)[0] - 1, cords[1])
	
	leak = fill(cords)
	while not leak:
		cords = (list(cords)[0] - 1, cords[1])
		leak = fill(cords)

	for l in leak:
		drop(l)

drop((0, 500))
print_ground()

ans = 0
for key, val in ground.items():
	if key[0] >= minimum and val in ['~', '|']:
		ans += 1

print(ans)