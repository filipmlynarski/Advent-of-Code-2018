import re
import numpy as np
from collections import defaultdict

puzzle = open('puzzle', 'r').read().splitlines()

plants = '....' + puzzle[0].strip().split()[-1] + '....'
left_most = -4

puzzle = {i.split(' => ')[0]: i.split(' => ')[1] for i in puzzle[2:]}
l = len(list(puzzle.keys())[0])
generations = 100

for g in range(generations):
	new_plants = ['.'] * len(plants)
	for i in range(len(plants)-l+1):
		if plants[i:i+l] in puzzle:
			new_plants[i+2] = puzzle[plants[i:i+l]]
		else:
			new_plants[i+2] = '.'
	

	pots_from_end = new_plants[::-1].index('#')
	if pots_from_end > 4:
		new_plants = new_plants[:-(pots_from_end-4)]
	elif pots_from_end < 4:
		new_plants.extend(['.'] * (4-pots_from_end))

	if '#' in new_plants[:4]:
		left_most -= 4-new_plants.index('#')
		new_plants = ['.']*(4-new_plants.index('#')) + new_plants
	elif new_plants[4] != '#':
		left_most += new_plants.index('#')-4
		new_plants = new_plants[new_plants.index('#')-4:]
	plants = ''.join(new_plants)
	print(plants)

ans = sum(idx+left_most for idx, i in enumerate(plants) if i == '#')
print(ans)