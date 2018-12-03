file = open('puzzle', 'r')
puzzle = file.read().splitlines()
file.close()

best = ''

for idx, i in enumerate(puzzle):
	for j in puzzle[idx+1:]:
		compared = ''.join([char1 for char1, char2 in zip(i, j) if char1 == char2])
		if len(compared) > len(best):
			best = compared

print(best)