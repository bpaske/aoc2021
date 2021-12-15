import math
from heapq import heappush, heappop

with open('./input.txt') as f:
    grid = [[int(i) for i in l.strip() ] for l in f.readlines()]
    initial_y = len(grid)
    initial_x = len(grid[0])
    max_y = initial_y*5
    max_x = initial_x*5
    enlarged_grid = [[0 for x in range(max_x)] for y in range(max_y)]
    for y in range(max_y):
        for x in range(max_x):
            candidate_value = (grid[y%initial_y][x%initial_x] + y//initial_y + x//initial_x)
            enlarged_grid[y][x] = (candidate_value + candidate_value // 10 ) %10

    distances = [[math.inf for _ in range(max_x)] for _ in range(max_y)]
    distances[0][0] = 0
    heap = [(0, (0,0))]
    vertex = None
    visited = set()

    while vertex != (max_y-1, max_x -1):
        distance, (current_y, current_x) = heappop(heap)
        if (current_y, current_x) in visited:
            continue

        for (y,x) in [(y,x) for (y,x) in [(current_y -1, current_x), (current_y+1, current_x), (current_y, current_x +1), (current_y, current_x-1)] if y >=0 and x >=0 and y<max_y and x< max_x]:
            candidate_distance = distances[current_y][ current_x] + enlarged_grid[y][x]
            if distances[y][x] > candidate_distance:
                distances[y][x] = candidate_distance
                heappush(heap, (candidate_distance, (y,x)))

        visited.add((current_y, current_x))
        vertex = (current_y, current_x)
    print(distances[max_y-1][max_x-1])

