import re
from collections import defaultdict

puzzle = open('puzzle', 'r').read().splitlines()
puzzle = [list(i) for i in puzzle]
#empty_grid = [i.replace('G', '#').replace('E', '#') for i in puzzle]

def distance(goblin, elf):
	return abs(elf[0] - goblin[0]) + abs(elf[1] - goblin[1])

def possible_moves(goblin):
	ret = []
	if puzzle[goblin[0]+1][goblin[1]] == '.':
		ret.append([goblin[0]+1, goblin[1]])
	if puzzle[goblin[0]][goblin[1]+1] == '.':
		ret.append([goblin[0], goblin[1]+1])
	if puzzle[goblin[0]-1][goblin[1]] == '.':
		ret.append([goblin[0]-1, goblin[1]])
	if puzzle[goblin[0]][goblin[1]-1] == '.':
		ret.append([goblin[0], goblin[1]-1])
	return ret

def best_move(moves, elves):
	sorted_moves = sorted(moves)
	
	best = [sorted_moves[0], 1e5]
	for move in sorted_moves:
		distances = [distance(move, i) for i in elves]
		if any(i < best[1] for i in distances):
			best = [move, min(distances)]

	return best

for _ in range(3):
	creatures = {}
	for y in range(len(puzzle)):
		for x in range(len(puzzle[y])):
			if puzzle[y][x] in ['E', 'G']:
				creatures[(y, x)] = [possible_moves([y, x]), puzzle[y][x]]

	for C in sorted(creatures.keys()):
		if not creatures[C][0]:
			continue

		oposite = []
		for creature in [i for i in creatures.keys() if creatures[i][1] != creatures[C][1]]:
			oposite.append(creature)

		move = best_move(creatures[C][0], oposite)
		if move[1] < min(distance(C, i) for i in oposite):
			puzzle[C[0]][C[1]] = '.'
			puzzle[move[0][0]][move[0][1]] = creatures[C][1]
			old = creatures[C].copy()
			#del creatures[C]
			#creatures[(move[0][0], move[0][1])] = [[], puzzle[move[0][0]][move[0][1]]]

			creatures = {}
			for y in range(len(puzzle)):
				for x in range(len(puzzle[y])):
					if puzzle[y][x] in ['E', 'G']:
						creatures[(y, x)] = [possible_moves([y, x]), puzzle[y][x]]

	print()
	for i in puzzle:
		print(''.join(i))
	#break