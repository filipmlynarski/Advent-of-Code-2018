from collections import defaultdict
import re

file = open('puzzle', 'r')
puzzle = file.read().splitlines()
file.close()

puzzle.sort()
guards = defaultdict(lambda :defaultdict(int))
worst_guard = [None, 0, 0]

for i in puzzle:
	if 'Guard' in i:
		guard = i.split()[3]
	if 'asleep' in i:
		asleep = int(re.findall(r'\d+', i)[4])
	if 'wakes' in i:
		awake = int(re.findall(r'\d+', i)[4])
		for x in range(asleep, awake):
			guards[guard][x] += 1

for guard_name in guards.keys():
	for k, v in guards[guard_name].items():
		if v > worst_guard[2]:
			worst_guard = int(guard_name[1:]), k, v

print(worst_guard[0] * worst_guard[1])