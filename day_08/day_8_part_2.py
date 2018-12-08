puzzle = open('puzzle', 'r').read().strip()
puzzle = list(map(int, puzzle.split()))

def get_nodes(x):
	child_nodes = x[0]
	metadata_entries = x[1]
	
	ret = []
	ret_sum = 0
	steps = 0
	
	for i in range(child_nodes):
		sub = get_nodes(x[2+steps:])
		ret.append(sub[0])
		steps += sub[1]
	
	if child_nodes == 0:
		ret_sum = sum(x[2+steps: 2+steps+metadata_entries])
	else:
		for v in x[2+steps: 2+steps+metadata_entries]:
			if v-1 < len(ret):
				ret_sum += ret[v-1]

	steps += 2 + metadata_entries
	return ret_sum, steps

print(get_nodes(puzzle)[0])