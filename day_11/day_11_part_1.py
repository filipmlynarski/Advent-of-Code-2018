import numpy as np

puzzle = open('puzzle', 'r').read().splitlines()

size = 300
serial = 42

def power(x, y):
	rack_id = x + 10
	fuel = (rack_id * y + serial) * rack_id
	return fuel // 100 % 10 - 5

grid = np.fromfunction(power, (size,size))

best = [None, 0]

for x in range(size - 3):
	for y in range(size - 3):
		s = np.sum(grid[y:y+3, x:x+3])
		if s > best[1]:
			best = [(x,y), s]

print(','.join(map(str,best[0])))