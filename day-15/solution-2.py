import heapq

risk_map = []

for line in open('input.txt'):
    risk_map.append([int(char) for char in line[:-1]])

prev = {(0, 0): (None, 0)}
queue = [(0, (0, 0))]

while True:
    (risk_sum, (x, y)) = heapq.heappop(queue)
    if (x, y) == (len(risk_map[0]) * 5 - 1, len(risk_map) * 5 - 1):
        print(risk_sum)
        break
    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if x + dx < 0 or y + dy < 0 or x + dx > len(risk_map[0]) * 5 - 1 or y + dy > len(risk_map) * 5 - 1:
            continue
        ori_x = (x + dx) % len(risk_map[0])
        add_x = (x + dx) // len(risk_map[0])
        ori_y = (y + dy) % len(risk_map)
        add_y = (y + dy) // len(risk_map)
        new_risk = risk_map[ori_y][ori_x] + add_x + add_y
        if new_risk > 9:
            new_risk %= 9
        new_risk_sum = risk_sum + new_risk
        if (x + dx, y + dy) in prev and new_risk_sum >= prev[(x + dx, y + dy)][1]:
            continue
        prev[(x + dx, y + dy)] = ((x, y), new_risk_sum)
        heapq.heappush(queue, (new_risk_sum, (x + dx, y + dy)))
