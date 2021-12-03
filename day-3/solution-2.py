line_count = 0
oxy = []
co2 = []
oxy_rate = [0] * 12
co2_rate = [0] * 12

for line in open("input.txt"):
    line_count += 1
    oxy.append(line.replace('\n', ''))
    co2.append(line.replace('\n', ''))

# time to start the good old nested loops

for index in range(12):
    if (len(oxy) > 1):
        oxy_sum = 0
        for line in oxy:
            oxy_sum += int(line[index])
        new_oxy = []
        for line in oxy:
            if (line[index] == str(int(oxy_sum / len(oxy) >= 0.5))):
                new_oxy.append(line)
        oxy = new_oxy
    
    if (len(co2) > 1):
        co2_sum = 0
        for line in co2:
            co2_sum += int(line[index])
        new_co2 = []
        for line in co2:
            if (line[index] == str(int(co2_sum / len(co2) < 0.5))):
                new_co2.append(line)
        co2 = new_co2

print(int(''.join(oxy), 2) * int(''.join(co2), 2))