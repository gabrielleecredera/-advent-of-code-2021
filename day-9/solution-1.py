heightmap = [] # y then x
counter = 0

for line in open("input.txt"):
    heightmap.append([int(char) for char in line[:-1]])

for x in range(len(heightmap[0])):
    for y in range(len(heightmap)):
        current = heightmap[y][x]
        up = down = left = right = 10
        if y > 0:
            left = heightmap[y - 1][x]
        if y < len(heightmap) - 1:
            right = heightmap[y + 1][x]
        if x > 0:
            up = heightmap[y][x - 1]
        if x < len(heightmap[0]) - 1:
            down = heightmap[y][x + 1]
        if current < up and current < down and current < left and current < right:
            counter += current + 1

print(counter)