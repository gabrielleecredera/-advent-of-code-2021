input = open('input-demo.txt').read().splitlines()
algo = input[0]
image = [[char for char in line] for line in input[2:]]
for turn in range(2):
    for line_i in range(len(image)):
        image[line_i] = ['.'] + image[line_i] + ['.']
    image.insert(0, ['.'] * len(image[0]))
    image.append(['.'] * len(image[0]))
    new_image = [row[:] for row in image]
    for y in range(len(image)):
        for x in range(len(image[0])):
            algo_index = []
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if x + dx < 0 or y + dy < 0 or x + dx > len(image[0]) - 1 or y + dy > len(image) - 1:
                        algo_index.append('0')
                    elif image[y + dy][x + dx] == '#':
                        algo_index.append('1')
                    else:
                        algo_index.append('0')
            new_image[y][x] = algo[int(''.join(algo_index), 2)]
    image = new_image
light_count = 0
for line in image:
    light_count += line.count('#')
print(light_count)