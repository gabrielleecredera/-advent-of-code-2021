import re

input = open('input.txt').read()
lines = [list(map(int, line)) for line in re.findall('(\d+),(\d+) -> (\d+),(\d+)', input)]
maximum = max([max(line) for line in lines])
counter = 0

# warning: inefficient xd, i did it the wrong way round
for x in range(maximum + 1):
    for y in range(maximum + 1):
        hit = 0
        for line in lines:
            if line[0] == line[2] or line[1] == line[3]:
                if (x <= max(line[0], line[2]) and x >= min(line[0], line[2]) and
                        y <= max(line[1], line[3]) and y >= min(line[1], line[3])):
                    hit += 1
                    if hit >= 2:
                        counter += 1
                        break
            else:
                if (x <= max(line[0], line[2]) and x >= min(line[0], line[2]) and
                        y <= max(line[1], line[3]) and y >= min(line[1], line[3]) and
                        (x - line[0])/(line[2] - line[0]) == (y - line[1])/(line[3] - line[1])):
                    hit += 1
                    if hit >= 2:
                        counter += 1
                        break

print(counter)