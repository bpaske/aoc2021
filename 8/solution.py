with open('./input.txt') as f:
    split_lines = [l.split('|') for l in f.readlines()]
    rhs = [rhs for [_,rhs] in split_lines]
    split_rhs = [s.strip() for r in rhs for s in r.split() ]
    print(split_rhs)
    print(sum(1 for s in split_rhs if len(s) in [2, 4, 3, 7]))
