with open('./input.txt') as f:
    numbers = [l.strip() for l in f]
    oxygen_candidates = numbers[:]
    for i in range(12):
        total_one_bits_at_i = sum([1 if n[i]== '1' else 0 for n in oxygen_candidates])
        most_common_bit_at_i = '0' if total_one_bits_at_i < len(oxygen_candidates) / 2 else '1'
        oxygen_candidates = [c for c in oxygen_candidates if c[i] == most_common_bit_at_i]
        if len(oxygen_candidates) == 1:
            break;
    co2_candidates = numbers[:]
    for i in range(12):
        total_one_bits_at_i = sum([1 if n[i]== '1' else 0 for n in co2_candidates])
        least_common_bit_at_i = '1' if total_one_bits_at_i < len(co2_candidates)/2 else '0'
        co2_candidates = [c for c in co2_candidates if c[i] == least_common_bit_at_i]
        if len(co2_candidates) == 1:
            break;

    print(co2_candidates)
    print(int(oxygen_candidates[0], base=2)*int(co2_candidates[0], base=2))
