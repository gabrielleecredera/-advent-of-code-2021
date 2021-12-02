hor = 0
depth = 0
aim = 0

for line in open("input.txt"):
    dir, dist = line.split(' ')
    if dir == 'forward':
        hor += int(dist)
        depth += aim * int(dist)
    if dir == 'up':
        aim -= int(dist)
    if dir == 'down':
        aim += int(dist)

print(hor * depth)