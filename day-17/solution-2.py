import re
from itertools import product

target_area = [[int(num) for num in pair] for pair in re.findall(r'(-?\d+)..(-?\d+)', open('input.txt').read())]
hit_count = 0
for ux in range(300):
    for uy in range(-500, 500):
        x = y = 0
        steps = 0
        vx = ux
        vy = uy
        in_range = False
        while True:
            steps += 1
            x += vx
            y += vy
            if vx > 0:
                vx -= 1
            vy -= 1
            if x > target_area[0][1]:
                break
            if y < target_area[1][0]:
                break
            if x >= target_area[0][0] and y <= target_area[1][1]:
                hit_count += 1
                break

print(hit_count)