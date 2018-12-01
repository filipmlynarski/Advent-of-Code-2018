file = open('puzzle', 'r')
puzzle = file.read().splitlines()
file.close()

x = sum(int(i) for i in puzzle)
print(x)