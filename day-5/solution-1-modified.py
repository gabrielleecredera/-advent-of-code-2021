import re
from collections import Counter

input = open('input.txt').read()
lines = [list(map(int, line)) for line in re.findall('(\d+),(\d+) -> (\d+),(\d+)', input)]
counter = Counter()

for line in lines:
    if line[0] == line[2]:
        for y in range(min(line[1], line[3]), max(line[1], line[3]) + 1):
            counter[(line[0], y)] += 1
    elif line[1] == line[3]:
        for x in range(min(line[0], line[2]), max(line[0], line[2]) + 1):
            counter[(x, line[1])] += 1

print(sum([count >= 2 for point, count in counter.items()]))