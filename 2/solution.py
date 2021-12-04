with open('./input.txt') as f:
    horizontal = 0
    depth = 0
    aim = 0

    for l in f.readlines():
        [direction, value] = l.split()

        if direction == 'forward':
            horizontal += int(value)
            depth += aim * int(value)
        elif direction == 'down':
            aim += int(value)
        elif direction == 'up':
            aim -= int(value)
        else:
            print('Unknown direction, %s', direction)


    print(horizontal*depth)
