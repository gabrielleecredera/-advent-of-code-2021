import re

def find_path(to_pts, current_path):
    for pt in to_pts:
        if pt.islower():
            double_count = 0
            for path_pt in current_path:
                if path_pt.islower() and current_path.count(path_pt) >= 2:
                    double_count += 1
            if double_count > 2:
                continue
        if pt == 'start':
            continue
        if pt == 'end':
            paths.append(current_path)
            continue
        # print(current_path + [pt])
        find_path(links[pt], current_path + [pt])

inputs = re.findall('([a-zA-Z]+)-([a-zA-Z]+)', open("input.txt").read())
links = {}
paths = []
for (input_from, input_to) in inputs:
    if input_from in links:
        links[input_from].append(input_to)
    else:
        links[input_from] = [input_to]
    if input_to in links:
        links[input_to].append(input_from)
    else:
        links[input_to] = [input_from]

find_path(links['start'], ['start'])
print(len(paths))