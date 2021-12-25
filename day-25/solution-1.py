map = []
f = open('input.txt').read().splitlines()
for line in f:
    map.append([char for char in line])
width = len(f[0])
height = len(f)

step = 0
while True:
    new_map = [line[:] for line in map]
    same = True
    step += 1
    for y, row in enumerate(map):
        for x, val in enumerate(row):
            if val == '>':
                if map[y][(x + 1) % width] == '.':
                    new_map[y][(x + 1) % width] = '>'
                    new_map[y][x] = '.'
                    same = False
    map = [line[:] for line in new_map]
    for y, row in enumerate(map):
        for x, val in enumerate(row):
            if val == 'v':
                if map[(y + 1) % height][x] == '.':
                    new_map[(y + 1) % height][x] = 'v'
                    new_map[y][x] = '.'
                    same = False
    map = [line[:] for line in new_map]
    if same:
        print(step)
        exit(1)