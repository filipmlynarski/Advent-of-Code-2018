idx1, idx2 = 0, 1
recipes = [3, 7]
generation = 20
inp = 939601

while len(recipes) < inp + 10:
	idx1 += 1 + recipes[idx1]
	idx1 %= len(recipes)
	idx2 += 1 + recipes[idx2]
	idx2 %= len(recipes)

	s = recipes[idx1] + recipes[idx2]
	recipes.extend(map(int, list(str(s))))

print(''.join(map(str, recipes[-10:])))
