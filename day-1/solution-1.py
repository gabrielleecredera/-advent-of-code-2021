increases = 0
last_depth = 0

for line in open("input.txt"):
    if int(line) > last_depth:
        increases += 1
    last_depth = int(line)

print(increases - 1)