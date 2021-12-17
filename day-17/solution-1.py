import re
from itertools import product

target_area = [[int(num) for num in pair] for pair in re.findall(r'(-?\d+)..(-?\d+)', open('input.txt').read())]
max_y = 0
for (ux, uy) in product(range(1, 300), repeat=2):
    x = y = 0
    steps = 0
    vx = ux
    vy = uy
    in_range = False
    temp_max_y = max_y
    while True:
        steps += 1
        x += vx
        y += vy
        if y > temp_max_y:
            temp_max_y = y
        if vx > 0:
            vx -= 1
        vy -= 1
        if x > target_area[0][1]:
            break
        if y < target_area[1][0]:
            break
        if x >= target_area[0][0] and y <= target_area[1][1]:
            if temp_max_y > max_y:
                max_y = temp_max_y
                break

print(max_y)