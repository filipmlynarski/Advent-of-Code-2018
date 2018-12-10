import re
import numpy as np
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

	grid = np.zeros(size, dtype=int)
	for p in points:
		x, y = p[0]-min_x, p[1]-min_y#+(size[0]//2)

		if 0 <= y < grid.shape[0] and 0 <= x < grid.shape[1]:
			grid[y, x] = 1
		else:
			if done:
				exit()
			break
	else:
		for i in grid:
			print(''.join(map(str,i)).replace('0', '.').replace('1', '#'))
		print(s)
		done = True
	
	new_points = defaultdict(list)
	for p, velocities in points.items():
		for velocity in velocities:
			new_cords = (p[0] + velocity[0], p[1] + velocity[1])
			new_points[new_cords].extend([velocity])
		
	points = new_points
	s += 1