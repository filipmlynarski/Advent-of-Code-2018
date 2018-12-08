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

while x:
	for k in sorted(x.keys()):
		if can_pop(k, x):
			for v in x[k]:
				if not v in x:
					x[v] = []
			del x[k]
			poped.append(k)
			break
print(''.join(poped))