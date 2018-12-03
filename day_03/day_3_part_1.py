import numpy as np

file = open('puzzle', 'r')
puzzle = file.read().splitlines()
file.close()

suit = np.zeros((1000, 1000))

for square in puzzle:
	square = square.split()[-2:]
	x, y = [int(i) for i in square[0][:-1].split(',')]
	width, height = [int(i) for i in square[1].split('x')]
	
	suit[y: y + height, x: x + width] += 1

for square in puzzle:
	claim_id = square.split()[0][1:]
	square = square.split()[-2:]
	x, y = [int(i) for i in square[0][:-1].split(',')]
	width, height = [int(i) for i in square[1].split('x')]
	
	if np.all(suit[y: y + height, x: x + width] == 1):
		print(claim_id)
		break

print(np.count_nonzero(suit>1))