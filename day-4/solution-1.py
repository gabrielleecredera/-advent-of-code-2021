import re

input = open("input.txt").read().splitlines()

numbers = re.findall('(\d+)', input[0])
boards = []

input.append('')
first = True
for line in input[1:]:
    if line == '':
        row_count = 0
        if not first:
            boards.append(temp_board_rows)
            boards.append(temp_board_cols)
        first = False
        temp_board_rows = []
        temp_board_cols = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]
        continue
    row = re.findall('(\d+)', line)
    temp_board_rows.append(row)
    for index, item in enumerate(row):
        temp_board_cols[index][row_count] = item
    row_count += 1

active_numbers = []
for turn in range(len(numbers) - 1):
    active_numbers.append(numbers[turn])
    for board in boards:
        for row in board:
            if all(item in active_numbers for item in row):
                board_sum = 0
                for row in board:
                    board_sum += sum(int(item) for item in row if item not in active_numbers)
                print(board_sum * int(active_numbers[-1]))
                exit(0)