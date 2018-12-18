from collections import defaultdict

puzzle = open('puzzle', 'r').read().splitlines()
grid = defaultdict(str)

for y in range(len(puzzle)):
	for x in range(len(puzzle[y])):
		grid[(y, x)] = puzzle[y][x]

def surrounding(cords, grid):
	ret = []
	for y in range(cords[0]-1, cords[0]+2):
		for x in range(cords[1]-1, cords[1]+2):
			if (y, x) != cords:
				ret.append(grid[(y, x)])
	return ret

minutes = 10

for m in range(minutes):
	old_grid = grid.copy()
	for y in range(len(puzzle)):
		for x in range(len(puzzle[y])):
			surr = surrounding((y, x), old_grid)
			this = grid[(y, x)]
			if this == '.' and surr.count('|') >= 3:
				grid[(y, x)] = '|'
			elif this == '|' and surr.count('#') >= 3:
				grid[(y, x)] = '#'
			elif this == '#' and (surr.count('#') == 0 or surr.count('|') == 0):
				grid[(y, x)] = '.'

print(list(grid.values()).count('|') * list(grid.values()).count('#'))