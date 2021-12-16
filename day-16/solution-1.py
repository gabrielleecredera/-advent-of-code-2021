version_sum = 0
global_index = 0

def decode_packet():
    global packet
    global version_sum
    global global_index
    version = int(packet[global_index:global_index + 3], 2)
    global_index += 3
    version_sum += version
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

    else:
        length_type = packet[global_index]
        global_index += 1
        read_count = 15 if length_type == '0' else 11
        length = int(packet[global_index:global_index + read_count], 2)
        global_index += read_count
        if length_type == '0':
            final_index = global_index + length
            while global_index < final_index:
                decode_packet()
        else:
            for sub_index in range(length):
                decode_packet()

input = open('input.txt').read()[:-1]
packet = bin(int(input, 16))[2:].zfill(len(input * 4))
decode_packet()
print(version_sum)