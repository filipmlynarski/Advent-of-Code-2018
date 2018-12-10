from collections import deque

players = [0] * 424
largest_marble = 71144
marbles = deque()
marbles.append(0)

for i in range(1, largest_marble+1):
    if i%23:
        marbles.rotate(2)
        marbles.append(i)
    else:
        marbles.rotate(-7)
        players[i%len(players)] += i + marbles.pop()

print(max(players))