import re
from itertools import permutations

counter = 0
allowed = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

for line in open('input.txt'):
    line = re.findall(r'[a-z]+', line)
    inputs = line[:-4]
    outputs = line[-4:]
    
    for comb in permutations('abcdefg'):
        mapping = {a:b for a,b in zip(comb, 'abcdefg')}
        new_inputs = [sorted(''.join([mapping[char] for char in input])) for input in inputs]
        if sum([''.join(input) in allowed for input in new_inputs]) == 10:
            counter += int(''.join([str(allowed.index(''.join(sorted(''.join([mapping[char] for char in output]))))) for output in outputs]))
            continue

print(counter) 