from itertools import chain

heightmap = [] # y then x
basin_groups = []

for line in open("input.txt"):
    heightmap.append([int(char) for char in line[:-1]])


for x in range(len(heightmap[0])):
    for y in range(len(heightmap)):
        if heightmap[y][x] != 9:
            new_group = True
            join_basins = []
            for index, basin in enumerate(basin_groups):
                if (x - 1, y) in basin or (x + 1, y) in basin or (x, y - 1) in basin or (x, y + 1) in basin:
                    join_basins.append(basin)
                    new_group = False
            if new_group:
                basin_groups.append([(x, y)])
            else:
                if (len(join_basins) > 1):
                    for basin in join_basins:
                        basin_groups.remove(basin)
                    basin_groups.append(list(set(chain.from_iterable(join_basins))) + [(x, y)])
                else:
                    basin_groups[basin_groups.index(join_basins[0])].append((x, y))
            

a  = sorted([len(basin) for basin in basin_groups])
print(a[-1] * a[-2] * a[-3])