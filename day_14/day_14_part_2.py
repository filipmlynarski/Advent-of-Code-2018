idx1, idx2 = 0, 1
recipes = [3, 7]
inp = '939601'
l = len(inp)
x = list(map(int, list(inp)))

while len(recipes) < l or recipes[-l:] != x:
	idx1 += 1 + recipes[idx1]
	idx1 %= len(recipes)
	idx2 += 1 + recipes[idx2]
	idx2 %= len(recipes)

	s = recipes[idx1] + recipes[idx2]
	if s >= 10:
		recipes.extend([s//10, s%10])
	else:
		recipes.append(s)

print(len(recipes)-l)