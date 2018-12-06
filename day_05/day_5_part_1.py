puzzle = open('puzzle', 'r').read().strip()

M = {}
for i in range(ord('a'), ord('z')+1):
	M[chr(i)] = chr(i).upper()
	M[chr(i).upper()] = chr(i)

stack = []
for i in puzzle:
	if stack and i == M[stack[-1]]:
		stack.pop()
	else:
		stack.append(i)

print(len(stack))