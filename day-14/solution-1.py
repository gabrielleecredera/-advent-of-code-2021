import re
from collections import Counter

template = [char for char in open('input.txt').read().splitlines()[0]]
rules = {a: b for (a, b) in re.findall(r'([A-Z][A-Z]) -> ([A-Z])', open('input.txt').read())}

for step in range(10):
    insert_count = 0
    for index in range(len(template) - 1):
        consider_pair = template[index + insert_count] + template[index + 1 + insert_count]
        if consider_pair in rules:
            template.insert(index + 1 + insert_count, rules[consider_pair])
            insert_count += 1

template = Counter(template).most_common()
print(template[0][1] - template[-1][1])