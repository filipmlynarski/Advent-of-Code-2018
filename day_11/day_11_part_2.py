import numpy as np

size = 300
grid = np.zeros((size, size), dtype=int)
serial = 2866

def fuel_at_cords(x, y):
	global serial
	rack_id = x + 10
	fuel = (rack_id * y + serial) * rack_id
	if fuel > 100:
		return int(str(int(fuel))[-3]) - 5
	return 0

for y in range(size):
	for x in range(size):
		grid[y][x] = fuel_at_cords(x, y)

best = [None, 0]
for square_size in range(1, size+1):
	for x in range(size - square_size):
		for y in range(size - square_size):
			s = np.sum(grid[y:y+square_size, x:x+square_size])
			if s > best[1]:
				best = [(x,y,square_size), s]

print(','.join(map(str,best[0])))