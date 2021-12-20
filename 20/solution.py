def process_grid(grid, mapping, default_element):
    grid_depth = len(grid)
    grid_width = len(grid[0])
    expanded_grid_width = grid_width+4
    expanded_grid_depth = grid_depth+4

    expanded_grid = [[default_element]* expanded_grid_width, [default_element]*expanded_grid_width] + [[default_element, default_element] + row + [default_element,default_element] for row in grid] + [[default_element]*expanded_grid_width, [default_element]*expanded_grid_width]

    processed_grid = [['0' for _ in range(expanded_grid_width)] for _ in range(expanded_grid_depth)]
    for y in range(expanded_grid_depth):
        for x in range(expanded_grid_width):
            binary_string = ''.join( [ expanded_grid[j][i] if j > 0 and i > 0 and j< expanded_grid_depth and i < expanded_grid_width else default_element  for j in range(y-1, y+2) for i in range(x-1, x+2)])
            processed_grid[y][x] = '1' if mapping[int(binary_string, 2)] == '#' else '0'
    return processed_grid

with open('./input.txt') as f:
    lines = f.readlines()
    mapping = [c for c in lines[0].strip()]

    grid = [['1' if c== '#' else '0' for c in l.strip()] for l in lines[2:]]

    processed_grid = process_grid(grid, mapping, '0')
    for i in range(49):
        processed_grid = process_grid(processed_grid, mapping, '0' if i%2 else '1')

    print(sum(int(i) for row in processed_grid for i in row))
