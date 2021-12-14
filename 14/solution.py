from collections import defaultdict, Counter
with open('./input.txt') as f:
    lines = f.readlines()
    template = lines[0].strip()
    insertions = defaultdict(str)

    for line in lines[1:]:
        [a,b] = line.split('->')
        insertions[a.strip()] = b.strip()

    for _ in range(10):
        new_template = template[0]
        for  (a,b) in zip(template, template[1:]):
            new_template +=  insertions[a+b] + b
        template = new_template

    counter = Counter(template)
    difference = counter.most_common()[0][1] - counter.most_common()[-1][1]
    print(difference)
