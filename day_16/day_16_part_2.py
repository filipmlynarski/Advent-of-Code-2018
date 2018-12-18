import re
from collections import defaultdict

puzzle = open('puzzle', 'r').read().splitlines()
finall_opcodes = [-1 for _ in range(16)]

while finall_opcodes.count(-1):
	for i in puzzle:

		if i.startswith('Before'):
			before = list(map(int, re.findall(r'-?\d+', i)))
		
		elif i.startswith('After'):
			after = list(map(int, re.findall(r'-?\d+', i)))

			opcodes = [-1] * 16
			Ar, Br, Cr = before[opcode[1]], before[opcode[2]], after[opcode[3]]
			code, Av, Bv = opcode[0], opcode[1], opcode[2]

			if Ar + Br == Cr and finall_opcodes[0] == -1:
				opcodes[0] = code
			if Ar + Bv == Cr and finall_opcodes[1] == -1:
				opcodes[1] = code
			
			if Ar * Br == Cr and finall_opcodes[2] == -1:
				opcodes[2] = code
			if Ar * Bv == Cr and finall_opcodes[3] == -1:
				opcodes[3] = code
			
			if Ar & Br == Cr and finall_opcodes[4] == -1:
				opcodes[4] = code
			if Ar & Bv == Cr and finall_opcodes[5] == -1:
				opcodes[5] = code
			
			if Ar | Br == Cr and finall_opcodes[6] == -1:
				opcodes[6] = code
			if Ar | Bv == Cr and finall_opcodes[7] == -1:
				opcodes[7] = code

			if Ar == Cr and finall_opcodes[8] == -1:
				opcodes[8] = code
			if Av == Cr and finall_opcodes[9] == -1:
				opcodes[9] = code


			if Cr == 1 and Av > Br and finall_opcodes[10] == -1:
				opcodes[10] = code
			elif Cr == 0 and Av <= Br and finall_opcodes[10] == -1:
				opcodes[10] = code

			if Cr == 1 and Ar > Bv and finall_opcodes[11] == -1:
				opcodes[11] = code
			elif Cr == 0 and Ar <= Bv and finall_opcodes[11] == -1:
				opcodes[11] = code

			if Cr == 1 and Ar > Br and finall_opcodes[12] == -1:
				opcodes[12] = code
			elif Cr == 0 and Ar <= Br and finall_opcodes[12] == -1:
				opcodes[12] = code


			if Cr == 1 and Av == Br and finall_opcodes[13] == -1:
				opcodes[13] = code
			elif Cr == 0 and Av != Br and finall_opcodes[13] == -1:
				opcodes[13] = code

			if Cr == 1 and Ar == Bv and finall_opcodes[14] == -1:
				opcodes[14] = code
			elif Cr == 0 and Ar != Bv and finall_opcodes[14] == -1:
				opcodes[14] = code

			if Cr == 1 and Ar == Br and finall_opcodes[15] == -1:
				opcodes[15] = code
			elif Cr == 0 and Ar != Br and finall_opcodes[15] == -1:
				opcodes[15] = code

			if opcodes.count(-1) == 15:
				idx, i = [[idx, i] for idx, i in enumerate(opcodes) if i != -1][0]
				finall_opcodes[idx] = i

		else:
			opcode = list(map(int, re.findall(r'-?\d+', i)))


puzzle = open('puzzle', 'r').read()
puzzle = puzzle[puzzle.index('\n\n\n')+4:].splitlines()

registers = [0] * 4
for i in puzzle:
	i = list(map(int, re.findall(r'-?\d+', i)))

	code = finall_opcodes.index(i[0])
	Ar, Br, Av, Bv, C = registers[i[1]], registers[i[2]], i[1], i[2], i[3]

	if code == 0:
		registers[C] = Ar + Br
	elif code == 1:
		registers[C] = Ar + Bv

	elif code == 2:
		registers[C] = Ar * Br
	elif code == 3:
		registers[C] = Ar * Bv

	elif code == 4:
		registers[C] = Ar & Br
	elif code == 5:
		registers[C] = Ar & Bv

	elif code == 6:
		registers[C] = Ar | Br
	elif code == 7:
		registers[C] = Ar | Bv

	elif code == 8:
		registers[C] = Ar
	elif code == 9:
		registers[C] = Av

	elif code == 10:
		if Av > Br:
			registers[C] = 1
		else:
			registers[C] = 0
	elif code == 11:
		if Ar > Bv:
			registers[C] = 1
		else:
			registers[C] = 0
	elif code == 12:
		if Ar > Br:
			registers[C] = 1
		else:
			registers[C] = 0

	elif code == 13:
		if Av == Br:
			registers[C] = 1
		else:
			registers[C] = 0
	elif code == 14:
		if Ar == Bv:
			registers[C] = 1
		else:
			registers[C] = 0
	elif code == 15:
		if Ar == Br:
			registers[C] = 1
		else:
			registers[C] = 0

print(registers[0])