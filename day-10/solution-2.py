import statistics

scores = []
points_map = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

for line in open('input.txt'):
    line = line[:-1]
    stack = []
    skip = False
    score = 0
    for char in line:
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        else:
            last = stack.pop()
            if ((last == '(' and char != ')')
                    or (last == '[' and char != ']')
                    or (last == '{' and char != '}')
                    or (last == '<' and char != '>')):
                skip = True
                break
    if skip:
        continue
    for char in stack[::-1]:
        score *= 5
        score += points_map[char]
    scores.append(score)

print(statistics.median(scores))