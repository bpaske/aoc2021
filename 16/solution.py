version_total = 0

def parse_literal_value(bits, start_bit):
    current_bit = start_bit
    bit_string = ''
    while True:
        next_bits = bits[current_bit: current_bit+5]
        bit_string += next_bits[1:]
        current_bit +=5
        if next_bits[0] == '0':
            break
    return current_bit, int(bit_string, 2)

def parse_operator_value(bits, start_bit):
    current_bit = start_bit
    length_type_id = bits[current_bit]
    current_bit +=1
    arguments = []
    if length_type_id == '0':
        total_length = int(bits[current_bit: current_bit+15], 2)
        current_bit += 15
        end_bit = current_bit + total_length
        while current_bit < end_bit:
            current_bit, value = parse_packet(bits, current_bit)
            arguments.append(value)

    else:
        amount_of_subpackets = int(bits[current_bit: current_bit+11], 2)
        current_bit +=11
        for _ in range(amount_of_subpackets):
            current_bit, value = parse_packet(bits, current_bit)
            arguments.append(value)
    return current_bit, arguments

def parse_packet(bits, start_bit):
    global version_total
    current_bit = start_bit
    version = int(bits[current_bit: current_bit+3], 2)
    version_total += version
    type_id = int(bits[current_bit+3: current_bit+6], 2)

    current_bit +=6
    if type_id == 4:
        return parse_literal_value(bits, current_bit)
    else:
        current_bit, arguments = parse_operator_value(bits, current_bit)
        if type_id == 0:
            return current_bit, sum(arguments)
        elif type_id == 1:
            return_value = 1
            for a in arguments:
                return_value *= a
            return current_bit, return_value
        elif type_id == 2:
            return current_bit, min(arguments)
        elif type_id == 3:
            return current_bit, max(arguments)
        elif type_id == 5:
            return current_bit, 1 if arguments[0] > arguments[1] else 0
        elif type_id == 6:
            return current_bit, 1 if arguments[0] < arguments[1] else 0
        elif type_id == 7:
            return current_bit, 1 if arguments[0] == arguments[1] else 0


with open('./input.txt') as f:
    chars = f.readline().strip()
    bits = "".join(format(int(char,16), '04b') for char in chars)

    current_bit = 0
    start_bit = current_bit
    current_bit, value = parse_packet(bits, current_bit)

    print(version_total)
    print(value)

