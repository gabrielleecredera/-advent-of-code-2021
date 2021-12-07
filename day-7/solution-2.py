import re
from collections import Counter

positions = Counter([int(x) for x in re.findall(r'(\d+)', open("input.txt").read())])
best_target = 0
best_cost = 9999999999999

for target in range(max(positions) + 1):
    cost = 0
    for position, count in positions.items():
        cost += count * abs(target - position) * (abs(target - position) + 1) / 2
    if (cost < best_cost):
        best_cost = cost
        best_target = target

print(best_cost)