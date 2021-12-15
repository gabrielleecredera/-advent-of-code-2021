import heapq

risk_map = []

for line in open('input.txt'):
    risk_map.append([int(char) for char in line[:-1]])

prev = {(0, 0): (None, 0)}
queue = [(0, (0, 0))]

# while True:
#     item = heapq.heappop(queue)[1]
#     for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         (x, y) = item
#         if x + dx < 0 or y + dy < 0 or x + dx > len(risk_map[0]) - 1 or y + dy > len(risk_map) - 1:
#             continue
#         risk_sum = prev[(x, y)][1] + risk_map[y + dy][x + dx]
#         if (x + dx, y + dy) not in prev or risk_sum < prev[(x + dx, y + dy)][1]:
#             prev[(x + dx, y + dy)] = ((x, y), risk_sum)
#         if (x + dx, y + dy) not in checked:
#             heapq.heappush(queue, (prev[(x + dx, y + dy)][1], (x + dx, y + dy)))
#     checked.add(item)
#     print(len(checked) / 1)
#     if item == (len(risk_map[0]) - 1, len(risk_map) - 1):
#         break

while True:
    (risk_sum, (x, y)) = heapq.heappop(queue)
    if (x, y) == (len(risk_map[0]) - 1, len(risk_map) - 1):
        print(risk_sum)
        break
    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if x + dx < 0 or y + dy < 0 or x + dx > len(risk_map[0]) - 1 or y + dy > len(risk_map) - 1:
            continue
        new_risk_sum = risk_sum + risk_map[y + dy][x + dx]
        if (x + dx, y + dy) in prev and new_risk_sum >= prev[(x + dx, y + dy)][1]:
            continue
        prev[(x + dx, y + dy)] = ((x, y), new_risk_sum)
        heapq.heappush(queue, (new_risk_sum, (x + dx, y + dy)))
