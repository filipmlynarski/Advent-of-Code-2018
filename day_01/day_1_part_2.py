file = open('puzzle', 'r')
puzzle = file.read().splitlines()
file.close()

done = False
x = 0
seen = {x}

while not done:
	for i in puzzle:
		x += int(i)
		if x in seen:
			done = True
			break
		seen.add(x)

print(x)