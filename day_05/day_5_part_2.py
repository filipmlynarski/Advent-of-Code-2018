puzzle = open('puzzle', 'r').read().strip()

M = {}
for i in range(ord('a'), ord('z')+1):
	M[chr(i)] = chr(i).upper()
	M[chr(i).upper()] = chr(i)

ans = len(puzzle)
for k in range(ord('a'), ord('z')+1):
	temp_puzzle = [i for i in puzzle if i not in [chr(k), M[chr(k)]]]
	stack = []
	for i in temp_puzzle:
		if stack and i == M[stack[-1]]:
			stack.pop()
		else:
			stack.append(i)
	ans = len(stack) if len(stack) < ans else ans

print(ans)