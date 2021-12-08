import re

counter = 0

for line in open('input.txt'):
    output = re.findall(r'[a-z]+', line)[-4:]
    for digit in output:
        if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
            counter += 1

print(counter) 