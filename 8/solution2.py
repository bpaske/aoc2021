def find_mappings_with_length(list, length):
    return [s for s in list if len(s) == length]

def calculate_number_from_line(line):
    [lhs, rhs] = line.split('|')
    signal_patterns = [sp.strip() for sp in lhs.split()]
    mappings={}
    one_mapping = find_mappings_with_length(signal_patterns, 2).pop()
    mappings["".join(sorted(one_mapping))] = '1'
    four_mapping = find_mappings_with_length(signal_patterns, 4).pop()
    mappings["".join(sorted(four_mapping))] = '4'
    seven_mapping = find_mappings_with_length(signal_patterns, 3).pop()
    mappings["".join(sorted(seven_mapping))] = '7'
    eight_mapping = find_mappings_with_length(signal_patterns, 7).pop()
    mappings["".join(sorted(eight_mapping))] = '8'
    zero_six_nine_mappings = find_mappings_with_length(signal_patterns, 6)
    six_mapping = [m for m in zero_six_nine_mappings if not all(l in m for l in one_mapping) ].pop()
    mappings["".join(sorted(six_mapping))] = '6'
    zero_nine_mapping = [m for m in zero_six_nine_mappings if m !=six_mapping]
    zero_mapping = [m for m in zero_nine_mapping if not all(l in m for l in four_mapping)].pop()
    mappings["".join(sorted(zero_mapping))] = '0'
    nine_mapping = [m for m in zero_nine_mapping if m != zero_mapping].pop()
    mappings["".join(sorted(nine_mapping))] ='9'
    two_three_five_mapping = find_mappings_with_length(signal_patterns, 5)
    three_mapping = [m for m in two_three_five_mapping  if all(l in m for l in one_mapping)].pop()
    mappings["".join(sorted(three_mapping))] ='3'
    two_five_mapping = [m for m in two_three_five_mapping if m != three_mapping]
    five_mapping = [m for m in two_five_mapping if all(l in nine_mapping for l in m)].pop()
    mappings["".join(sorted(five_mapping))] = '5'
    two_mapping =[m for m in two_five_mapping if m != five_mapping].pop()
    mappings["".join(sorted(two_mapping))] ='2'

    value ="".join( (mappings["".join(sorted(i.strip()))] for i in rhs.split()))
    return int(value)



with open('./input.txt') as f:
    print(sum(calculate_number_from_line(l) for l in f.readlines()))
