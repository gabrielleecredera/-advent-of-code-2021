hor = 0
depth = 0

for line in open("input-1.txt"):
    dir, dist = line.split(' ')
    if dir == 'forward':
        hor += int(dist)
    if dir == 'up':
        depth -= int(dist)
    if dir == 'down':
        depth += int(dist)

print(hor * depth)