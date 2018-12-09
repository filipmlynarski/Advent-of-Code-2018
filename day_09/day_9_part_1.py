puzzle = open('puzzle', 'r').read().splitlines()

marbles = [0, 1]
amount_of_marbles = 71144
players = [0 for _ in range(424)]
current_pos = 1

for idx in range(2, amount_of_marbles+1):

	if idx%23 == 0:
		players[idx%len(players)] += idx
		players[idx%len(players)] += marbles.pop(current_pos-7)
		
		current_pos -= 7
		current_pos %= len(marbles)+1
	else:
		current_pos += 2
		if current_pos > len(marbles):
			current_pos %= len(marbles)
		marbles.insert(current_pos, idx)

print(max([[idx, i] for idx, i in enumerate(players)], key=lambda x: x[1]))