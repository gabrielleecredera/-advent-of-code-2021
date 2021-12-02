import re

input = open("input-1.txt").read()
hor = sum(map(int, re.findall('forward (\d+)', input)))
depth = sum(map(int, re.findall('down (\d+)', input))) - sum(map(int, re.findall('up (\d+)', input)))
print(hor * depth)