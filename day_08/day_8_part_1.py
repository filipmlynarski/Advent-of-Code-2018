puzzle = open('puzzle', 'r').read().strip()
puzzle = list(map(int, puzzle.split()))

headers = 0

def get_nodes(x):
	global headers

	child_nodes = x[0]
	metadata_entries = x[1]
	steps = 0
	
	for i in range(child_nodes):
		steps += get_nodes(x[2+steps:])
	
	headers += sum(x[2+steps: 2+steps+metadata_entries])
	steps += 2 + metadata_entries

	return steps

get_nodes(puzzle)
print(headers)