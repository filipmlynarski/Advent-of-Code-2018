import re
from collections import defaultdict

puzzle = open('puzzle', 'r').read().splitlines()
puzzle = [list(map(int, re.findall(r'-?\d+', i))) for i in puzzle]
points = {tuple(i[:2]): [i[2:]] for i in puzzle}

import os
size = list(map(int, [os.popen('tput lines').read(), os.popen('tput cols').read()]))

s = 0
done = False
while True:
	min_x = min(points.keys(), key=lambda x: x[0])[0]
	min_y = min(points.keys(), key=lambda x: x[1])[1]

	grid = [['.']*size[1] for _ in range(size[0])]
	for p in points:
		x, y = p[0]-min_x, p[1]-min_y#+(size[0]//2)

		if 0 <= y < size[0] and 0 <= x < size[1]:
			grid[y][x] = '#'
		else:
			if done:
				exit()
			break
	else:
		for i in grid:
			print(''.join(i))
		print(s)
		done = True
	
	new_points = defaultdict(list)
	for p, velocities in points.items():
		for velocity in velocities:
			new_cords = (p[0] + velocity[0], p[1] + velocity[1])
			new_points[new_cords].extend([velocity])
		
	points = new_points
	s += 1