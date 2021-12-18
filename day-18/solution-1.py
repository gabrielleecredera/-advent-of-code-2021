import re
import math

def explode(input):
    nest_count = 0
    for char_i, char in enumerate(input):
        if char == '[':
            nest_count += 1
            if nest_count == 5:
                start_pos = char_i
                for char_a in input[start_pos:]:
                    check_pair = input[start_pos:start_pos + 5]
                    if check_pair[0] == '[' and isinstance(check_pair[1], int) and check_pair[2] == ',' and isinstance(check_pair[3], int) and check_pair[4] == ']':
                        break
                    else:
                        start_pos += 1
                end_pos = start_pos + 4
                right_pos = None
                for pos in range(end_pos, len(input)):
                    if isinstance(input[pos], int):
                        right_pos = pos
                        break
                if right_pos:
                    # print(''.join([str(char) for char in input[start_pos:]]))
                    input[right_pos] = input[start_pos + 3] + input[right_pos]
                left_pos = None
                for pos in range(0, start_pos):
                    if isinstance(input[start_pos - pos], int):
                        left_pos = start_pos - pos
                        break
                if left_pos:
                    input[left_pos] = input[start_pos + 1] + input[left_pos]
                input[start_pos:end_pos + 1] = [0]
                return input
        elif char == ']':
            nest_count -= 1
    return None

def split(input):
    for char_i, char in enumerate(input):
        if isinstance(char, int) and char >= 10:
            input = input[:char_i] + ['['] + [int(math.floor(char / 2))] + [','] + [int(math.ceil(char / 2))] + [']'] + input[char_i + 1:]
            return input
    return None

nums = open('input.txt').read().splitlines()
for num_i, num in enumerate(nums):
    nums[num_i] = [(int(char) if char.isnumeric() else char) for char in re.findall(r'\[|,|\]|\d+', num)]
current = nums[0]
for num_i in range(1, len(nums)):
    current = ['['] + current + [','] + nums[num_i] + [']']
    while True:
        no_explode = True
        no_split = True
        while True:
            explode_r = explode(current)
            if explode_r:
                current = explode_r
                no_explode = False
            else:
                break
        split_r = split(current)
        if split_r:
            current = split_r
            no_split = False
        if no_explode and no_split:
            break
current = ''.join([str(char) for char in current])
while True:
    old_current = current
    current = re.sub(r'\[(\d+),(\d+)\]', lambda match: str(int(match.group(1)) * 3 + int(match.group(2)) * 2), current)
    if old_current == current:
        print(current)
        exit(1)
