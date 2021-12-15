import math
import heapq

with open('./input.txt') as f:
    grid = [[int(i) for i in l.strip() ] for l in f.readlines()]
    max_y = len(grid)
    max_x = len(grid[0])
    distances = [[math.inf for _ in row] for row in grid]
    distances[0][0] = 0
    vertex = None
    visted = set()

    while vertex != (max_y-1, max_x -1):
        next_distance = math.inf
        for y, row in enumerate(distances):
            for  x, distance in enumerate(row):
                if (y, x) not in visted and distance < next_distance:
                    vertex = (y, x)
                    next_distance = distance

        for (y,x) in [(y,x) for (y,x) in [(vertex[0] -1, vertex[1]), (vertex[0]+1, vertex[1]), (vertex[0], vertex[1] +1), (vertex[0], vertex[1]-1)] if y >=0 and x >=0 and y<max_y and x< max_x]:
            distances[y][x] = min(distances[y][x], distances[vertex[0]][ vertex[1]] + grid[y][x])
        visted.add(vertex)
    print(distances[max_y-1][max_x-1])

