puzzle = open('puzzle', 'r').read().splitlines()

def clear(inp):
	ret = []
	players = []
	for y in range(len(inp)):
		ret.append([])
		for x in range(len(inp[y])):
			if inp[y][x] in ['>', '<']:
				players.append([[y, x], inp[y][x], 0])
				ret[-1].append('-')
			elif inp[y][x] in ['^', 'v']:
				players.append([[y, x], inp[y][x], 0])
				ret[-1].append('|')
			else:
				ret[-1].append(inp[y][x])
	return ret, players

def print_track():
	for y in range(len(track)):
		for x in range(len(track[y])):
			player = [i for i in players if [y, x] == i[0]]
			if len(player):
				print(player[0][1], end='')
			else:
				print(track[y][x], end='')
		print()

def move(player):
	if player[1] == '>':
		player[0][1] += 1
	elif player[1] == '<':
		player[0][1] -= 1
	elif player[1] == '^':
		player[0][0] -= 1
	elif player[1] == 'v':
		player[0][0] += 1
	return player

turns = [{'>': '^', '^': '<', '<': 'v', 'v': '>'},
		 {'>': '>', 'v': 'v', '<': '<', '^': '^'},
		 {'>': 'v', 'v': '<', '<': '^', '^': '>'}]

track, players = clear(puzzle)

while True:
	to_pop = []
	for player in sorted(players, key=lambda x: x[0]):
		if player in [players[i] for i in to_pop]:
			continue

		if track[player[0][0]][player[0][1]] == '\\':
			if player[1] == '>':
				player[1] = 'v'
			elif player[1] == '^':
				player[1] = '<'
			elif player[1] == '<':
				player[1] = '^'
			elif player[1] == 'v':
				player[1] = '>'

		elif track[player[0][0]][player[0][1]] == '/':
			if player[1] == '>':
				player[1] = '^'
			elif player[1] == '^':
				player[1] = '>'
			elif player[1] == '<':
				player[1] = 'v'
			elif player[1] == 'v':
				player[1] = '<'

		elif track[player[0][0]][player[0][1]] == '+':
			player[1] = turns[player[2]][player[1]]
			player[2] = (player[2] + 1) % len(turns)

		player = move(player)
		
		if [i[0] for i in players].count(player[0]) > 1:
			for idx in range(len(players)):
				if players[idx][0] == player[0]:
					to_pop.append(idx)

	for idx in sorted(to_pop, reverse=True):
		players.pop(idx)

	if len(players) == 1:
		print(','.join(map(str, players[0][0][::-1])))
		break