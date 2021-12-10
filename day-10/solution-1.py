counter = 0
points_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

for line in open('input.txt'):
    line = line[:-1]
    stack = []
    for char in line:
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        else:
            last = stack.pop()
            if ((last == '(' and char != ')')
                    or (last == '[' and char != ']')
                    or (last == '{' and char != '}')
                    or (last == '<' and char != '>')):
                counter += points_map[char]
                break

print(counter)