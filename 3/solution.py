with open('./input.txt') as f:
    numbers = [int(l, base=2) for l in f]
    most_common_bits =0
    for i in range(12):
        total_one_bits_at_i = sum([(n & 1 << i) >> i for n in numbers])
        if total_one_bits_at_i > 500:
            most_common_bits += 1 << i
    least_common_bits = most_common_bits ^ (2 ** 12 -1)
    print(least_common_bits * most_common_bits)
