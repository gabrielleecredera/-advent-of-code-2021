import re

input = re.findall(r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', open('input.txt').read())
cubes = set()

for step in input:
    step = [int(x) if x.strip('-').isnumeric() else x for x in step]
    [op, ux, vx, uy, vy, uz, vz] = step
    if min(ux, vx) > 50 or max(ux, vx) < -50 or min(uy, vy) > 50 or max(uy, vy) < -50 or min(uz, vz) > 50 or max(uz, vz) < -50:
        break
    for x in range(min(ux, vx), max(ux, vx) + 1):
        for y in range(min(uy, vy), max(uy, vy) + 1):
            for z in range(min(uz, vz), max(uz, vz) + 1):
                if op == 'on':
                    cubes.add((x, y, z))
                else:
                    try:
                        cubes.remove((x, y, z))
                    except KeyError:
                        continue
print(len(cubes))