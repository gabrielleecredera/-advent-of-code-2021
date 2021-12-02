increases = 0
last_depth_sum = 0

depths = [int(depth) for depth in open("input.txt").read().splitlines()]

for index, depth in enumerate(depths):
    if index == len(depths) - 2:
        break
    depth_sum = depth + depths[index + 1] + depths[index + 2]
    if depth_sum > last_depth_sum:
        increases += 1
    last_depth_sum = depth_sum

print(increases - 1)