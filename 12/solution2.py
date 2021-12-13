from collections import defaultdict, Counter, deque

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
        if node != 'start' and (node.isupper() or can_vist_small_cave(partial_solution, node)):
            backtrack(adjacency_list, partial_solution+[node], solutions);


def can_vist_small_cave(partial_solution, node):
    if node == 'end':
        return True
    counts = Counter([p for p in partial_solution if p.islower()])
    top_count = counts.most_common(1)[0][1] if len(counts) > 0 else 0
    return counts[node] == 0 or (counts[node] == 1 and top_count < 2)

with open('./input.txt') as f:
    adjacency_list = build_graph(f.readlines())

    solutions = []
    backtrack(adjacency_list, ['start'], solutions)
    print(len(solutions))
