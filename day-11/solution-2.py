octs = [] # y then x
flashes = 0

def trigger_flashes(x, y):
    if octs[y][x] <= 9 or (x, y) in flashed:
        return
    flashed.append((x, y))
    for (target_x, target_y) in [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]:
        if target_x < 0 or target_y < 0 or target_x > len(octs[0]) - 1 or target_y > len(octs) - 1:
            continue
        octs[target_y][target_x] += 1
        if (target_x, target_y) not in flashed:
            trigger_flashes(target_x, target_y)

for line in open('input.txt'):
    octs.append([int(char) for char in line[:-1]])

for step in range(9999):
    flashed = []
    for y in range(len(octs)):
        for x in range(len(octs[0])):
            octs[y][x] += 1
    for y in range(len(octs)):
        for x in range(len(octs[0])):
            trigger_flashes(x, y)
    old_flash = flashes
    for y in range(len(octs)):
        for x in range(len(octs[0])):
            if octs[y][x] > 9:
                flashes += 1
                octs[y][x] = 0
    if flashes - old_flash == len(octs) * len(octs[0]):
        print(step + 1)
        break


