rows = 0
sums = [0] * 12

for line in open("input.txt"):
    rows += 1
    for index, char in enumerate(line):
        if char == '\n':
            continue
        sums[index] += int(char)

gamma = int(''.join([str(int(sum/rows > 0.5)) for sum in sums]), 2)
epsilon = int(''.join([str(int(sum/rows < 0.5)) for sum in sums]), 2)

print(gamma * epsilon)