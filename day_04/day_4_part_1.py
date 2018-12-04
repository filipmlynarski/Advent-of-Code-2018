from collections import defaultdict
import re

file = open('puzzle', 'r')
puzzle = file.read().splitlines()
file.close()

puzzle.sort()
guards = defaultdict(int)

for i in puzzle:
	if 'Guard' in i:
		guard = i.split()[3]
	if 'asleep' in i:
		asleep = list(map(int, re.findall(r'\d+', i)))[4]
	if 'wakes' in i:
		awake = list(map(int, re.findall(r'\d+', i)))[4]
		guards[guard] += awake - asleep

worst_guard = max(guards.items(), key=lambda x: x[1])
guard_asleep = defaultdict(int)

for i in puzzle:
	if 'Guard' in i:
		guard = i.split()[3]
	if guard != worst_guard[0]:
		continue
	
	if 'asleep' in i:
		asleep = list(map(int, re.findall(r'\d+', i)))[4]
	elif 'wakes' in i:
		awake = list(map(int, re.findall(r'\d+', i)))[4]
		for x in range(asleep, awake):
			guard_asleep[x] += 1

print(int(worst_guard[0][1:]) * max(guard_asleep.keys(), key=lambda x:guard_asleep[x]))