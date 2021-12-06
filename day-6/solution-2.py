import re
from collections import Counter

states = [int(x) for x in re.findall(r'(\d+)', open('input.txt').read())]
counter = Counter(states)

for day in range(256):
    new_counter = Counter()
    for state, count in counter.items():
        new_state = state - 1
        if (new_state < 0):
            new_counter[8] += count
            new_state += 7
        new_counter[new_state] += count
    counter = new_counter

print(sum(counter.values()))