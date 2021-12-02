increases = 0
last_depth_sum = 0

depths = [int(depth) for depth in open("input.txt").read().splitlines()]

for depths in zip(depths, depths[1:], depths[2:]):
    if sum(depths) > last_depth_sum:
        increases += 1
    last_depth_sum = sum(depths)

print(increases - 1)