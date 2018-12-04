import numpy as np
import re

file = open('puzzle', 'r')
puzzle = file.read().splitlines()
file.close()

suit = np.zeros((1000, 1000))

for square in puzzle:
	ID, x, y, width, height = map(int, re.findall(r'-?\d+', square))
	suit[y: y + height, x: x + width] += 1

print(np.count_nonzero(suit>1))