from collections import defaultdict, Counter
with open('./input.txt') as f:
    lines = f.readlines()
    template = lines[0].strip()
    insertions = {}

    for line in lines[1:]:
        [a,b] = line.split('->')
        insertions[a.strip()] = b.strip()

    counter = Counter(template)
    pair_counter= Counter(x+y for (x,y) in zip(template, template[1:]))

    for _ in range(40):
        new_pair_counter = Counter(pair_counter)
        for (pair, count) in pair_counter.items():
            if pair in insertions:
                middle_value = insertions[pair]
                new_pair_counter[pair[0]+middle_value] += count
                new_pair_counter[middle_value + pair[1]] += count
                new_pair_counter[pair] -= count
                counter[middle_value] += count
        pair_counter = new_pair_counter

    difference = counter.most_common()[0][1] - counter.most_common()[-1][1]
    print(difference)
