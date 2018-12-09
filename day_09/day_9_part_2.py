puzzle = open('puzzle', 'r').read().splitlines()

marbles = [0, 1]
amount_of_marbles = 71144*100
players = [0 for _ in range(424)]
current_pos = 1
prcnt = -1

for idx in range(2, amount_of_marbles+1):
	if int((idx/(amount_of_marbles+1))*100) != prcnt:
		print(int((idx/(amount_of_marbles+1))*100)+1, '%')
		prcnt = int((idx/(amount_of_marbles+1))*100)
	
	if idx%23 == 0:
		players[idx%len(players)] += idx
		if current_pos-7 < 0:
			players[idx%len(players)] += marbles.pop((current_pos-7) % (len(marbles)+1))
		else:
			players[idx%len(players)] += marbles.pop(current_pos-7)
		current_pos -= 7
		if current_pos-7 < 0:
			current_pos %= (len(marbles)+1)
	else:
		current_pos += 2
		if current_pos > len(marbles):
			current_pos %= len(marbles)
		marbles.insert(current_pos, idx)

	#str_marbles = list(map(str,marbles))
	#str_marbles[current_pos] = '(' + str_marbles[current_pos] + ')'
	#print('[{}] {}'.format((idx-1)%len(players)+1, '  '.join(str_marbles)))

print(max([[idx, i] for idx, i in enumerate(players)], key=lambda x: x[1])) #[74, 3411514667] in just 3hours!