file = open('puzzle', 'r')
puzzle = file.read().splitlines()
file.close()

x = [[0 for _ in range(len(puzzle))] for i in range(2)]

for idx, i in enumerate(puzzle):
	for char in set(i):
		if i.count(char) == 2:
			x[0][idx] = 1
		elif i.count(char) == 3:
			x[1][idx] = 1

print(sum(x[0]) * sum(x[1]))