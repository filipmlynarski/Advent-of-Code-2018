import os
import time

total_runtime = 0

for dir_name in [i for i in os.listdir('.') if os.path.isdir(i) and i != '.git']:
	day = str(int(dir_name.split('_')[-1]))
	for part in range(1, 3):
		start = time.time()
		output = os.popen('cd {}; python3 day_{}_part_{}.py; cd ..'.format(dir_name, day, part)).read()
		total_time = time.time() - start
		total_runtime += total_time
		print('[{:<6}s] day{} part{} output: {}'.format(round(total_time, 4), day, part, output[:-1]))
	print()

print('Total runtime: {}s'.format(round(total_runtime, 3)))
