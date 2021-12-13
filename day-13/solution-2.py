import re

dots = [(int(a), int(b)) for (a, b) in re.findall(r'(\d+),(\d+)', open('input.txt').read())]
folds = [(a, int(b)) for (a, b) in re.findall(r'([xy])=(\d+)', open('input.txt').read())]

for fold in folds:
    max_pt = fold[1] * 2
    axis_index = 0 if fold[0] == 'x' else 1
    for dot_i, dot in enumerate(dots):
        if dot[axis_index] > fold[1]:
            if axis_index:
                dots[dot_i] = (dot[0], max_pt - dots[dot_i][axis_index])
            else:
                dots[dot_i] = (max_pt - dots[dot_i][axis_index], dot[1])
    dots = list(set(dots))

# inverted printing cuz it's a transparent paper lol, took me 5 tries...
max_x = max_y = 0
for dot in dots:
    if dot[0] > max_x:
        max_x = dot[0]
    if dot[1] > max_y:
        max_y = dot[1]
for x in range(max_y + 1):
    for y in range(max_x + 1):
        if (y, x) in dots:
            print('#', end="")
        else:
            print('.', end="")
    print()