import re
from collections import defaultdict

puzzle = open('puzzle', 'r').read().splitlines()
total = 0

for i in puzzle:
	if i.startswith('Before'):
		before = list(map(int, re.findall(r'-?\d+', i))) 
	
	elif i.startswith('After'):
		after = list(map(int, re.findall(r'-?\d+', i))) 

		Ar, Br, Cr = before[opcode[1]], before[opcode[2]], after[opcode[3]]
		Av, Bv = opcode[1], opcode[2]
		ans = 0

		if Ar + Br == Cr:
			ans += 1
		if Ar + Bv == Cr:
			ans += 1
		
		if Ar * Br == Cr:
			ans += 1
		if Ar * Bv == Cr:
			ans += 1
		
		if Ar & Br == Cr:
			ans += 1
		if Ar & Bv == Cr:
			ans += 1
		
		if Ar | Br == Cr:
			ans += 1
		if Ar | Bv == Cr:
			ans += 1

		if Ar == Cr:
			ans += 1 
		if Av == Cr:
			ans += 1


		if Cr == 1 and Av > Br:
			ans += 1
		elif Cr == 0 and Av <= Br:
			ans += 1

		if Cr == 1 and Ar > Bv:
			ans += 1
		elif Cr == 0 and Ar <= Bv:
			ans += 1

		if Cr == 1 and Ar > Br:
			ans += 1
		elif Cr == 0 and Ar <= Br:
			ans += 1


		if Cr == 1 and Av == Br:
			ans += 1
		elif Cr == 0 and Av != Br:
			ans += 1

		if Cr == 1 and Ar == Bv:
			ans += 1
		elif Cr == 0 and Ar != Bv:
			ans += 1

		if Cr == 1 and Ar == Br:
			ans += 1
		elif Cr == 0 and Ar != Br:
			ans += 1

		total += ans >= 3
	
	else:
		opcode = list(map(int, re.findall(r'-?\d+', i)))

print(total)