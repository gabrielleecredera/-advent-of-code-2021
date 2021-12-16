global_index = 0

def decode_packet():
    global packet
    global global_index
    version = int(packet[global_index:global_index + 3], 2)
    global_index += 3
    type_id = int(packet[global_index:global_index + 3], 2)
    global_index += 3
    if type_id == 4:
        num = []
        while True:
            lead = packet[global_index]
            num += packet[global_index + 1:global_index + 5]
            global_index += 5
            if lead == '0':
                break
        return int(''.join(num), 2)

    else:
        length_type = packet[global_index]
        global_index += 1
        read_count = 15 if length_type == '0' else 11
        length = int(packet[global_index:global_index + read_count], 2)
        global_index += read_count
        values = []
        if length_type == '0':
            final_index = global_index + length
            while global_index < final_index:
                values.append(decode_packet())
        else:
            for sub_index in range(length):
                values.append(decode_packet())
        if type_id == 0:
            return sum(values)
        elif type_id == 1:
            prod_result = 1
            for value in values:
                prod_result *= value
            return prod_result
        elif type_id == 2:
            return min(values)
        elif type_id == 3:
            return max(values)
        elif type_id == 5:
            return int(values[0] > values[1])
        elif type_id == 6:
            return int(values[0] < values[1])
        elif type_id == 7:
            return int(values[0] == values[1])

input = open('input.txt').read()[:-1]
packet = bin(int(input, 16))[2:].zfill(len(input * 4))
print(decode_packet())