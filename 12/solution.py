from collections import defaultdict, Counter

def build_graph(lines):
    adjacency_list = defaultdict(list)

    for l in lines:
        [x,y] = l.strip().split('-')
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)

    return adjacency_list

def backtrack(adjacency_list, partial_solution, solutions):
    current_node = partial_solution[-1]
    if current_node == 'end':
        solutions.append(partial_solution)
        return

    for node in adjacency_list[current_node]:
        if node.isupper() or node not in partial_solution:
            backtrack(adjacency_list, partial_solution+[node], solutions);

with open('./small-input.txt') as f:
    adjacency_list = build_graph(f.readlines())
    solutions = []
    results = backtrack(adjacency_list, ['start'], solutions)
    print(len(solutions))
