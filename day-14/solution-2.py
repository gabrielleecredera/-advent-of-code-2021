import re
from collections import Counter

template_input = open('input.txt').read().splitlines()[0]
template = [char for char in template_input]
template = Counter(zip(template[:-1], template[1:]))
rules = {a: b for (a, b) in re.findall(r'([A-Z][A-Z]) -> ([A-Z])', open('input.txt').read())}

for step in range(40):
    template_c = Counter(template)
    for pair in template_c:
        if template_c[pair] == 0:
            continue
        if pair[0] + pair[1] in rules:
            template[pair] -= template_c[pair]
            template[(pair[0], rules[pair[0] + pair[1]])] += template_c[pair]
            template[(rules[pair[0] + pair[1]], pair[1])] += template_c[pair]

char_count = Counter()
for pair in template.items():
    char_count[pair[0][0]] += pair[1]
    char_count[pair[0][1]] += pair[1]
char_count[template_input[0]] += 1
char_count[template_input[-1]] += 1
for char in char_count:
    char_count[char] /= 2
char_count = Counter(char_count).most_common()
print(char_count[0][1] - char_count[-1][1])