empty = '.'
east = '>'
south = 'v'

with open('./input.txt') as f:
    initial_state = [[c for c in line.strip()] for line in f.readlines()]
    height = len(initial_state)
    width = len(initial_state[0])

    modified = True
    counter = 0
    state = initial_state
    while modified:
        modified = False
        counter += 1
        next_state = [[empty for _ in range(width)] for _ in range(height)]

        for y, row in enumerate(state):
            for x, item in enumerate(row):
                if item == east:
                    if state[y][(x+1)%width] == empty:
                        next_state[y][(x+1)%width] = east
                        modified = True
                    else:
                        next_state[y][x] = east

        for y, row in enumerate(state):
            for x, item in enumerate(row):
                if item == south:
                    if next_state[(y+1)%height][x] == empty and state[(y+1)%height][x] != south:
                        next_state[(y+1)%height][x] = south
                        modified = True
                    else:
                        next_state[y][x] = south
        state = next_state

print(counter)
