puzzle = open('puzzle', 'r').read().splitlines()
x = {}

for i in puzzle:
	i = i.split()
	a, b = i[1], i[-3]
	if not i[1] in x:
		x[a] = []
	x[a].append(b)

def can_pop(x, y):
	for i in y.values():
		if x in i:
			return False
	return True

poped = []
workers = [False for _ in range(5)]
seconds = 0

while True:
	for idx, worker in enumerate(workers):
		to_add = []
		if worker and list(worker.values())[0] == 0:
			k = list(worker.keys())[0]
			for v in x[k]:
				if not v in x:
					x[v] = []
			del x[k]
			to_add.append(k)
			workers[idx] = False
		poped.extend(to_add)

	if not x:
		break

	for k in sorted(x.keys()):
		if k not in [list(i.keys())[0] for i in workers if i] and not all(workers) and can_pop(k, x):
			workers[workers.index(False)] = {k: 60 + ord(k) - ord('A') + 1}

	for idx in range(len(workers)):
		if workers[idx]:
			k = list(workers[idx].keys())[0]
			workers[idx][k] -= 1
	seconds += 1

print(seconds)