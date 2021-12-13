import re

def fold_x(points, x_fold):
    left_points = {(x,y) for (x,y) in  points if x < x_fold}
    right_points = {(x,y) for (x,y) in  points if x > x_fold}
    for (x,y) in right_points:
        left_points.add((x_fold-(x-x_fold), y))
    return left_points

def fold_y(points, y_fold):
    top_points = {(x,y) for (x,y) in  points if y < y_fold}
    bottom_points = {(x,y) for (x,y) in  points if y > y_fold}
    for (x,y) in bottom_points:
        top_points.add((x, y_fold - (y-y_fold)))
    return top_points

with open('./input.txt') as f:
    lines = list(f.readlines())

    points = set()
    folds = []

    for line in lines:
        if re.match(r"\d+,\d+", line):
            [x,y] = line.strip().split(',')
            points.add((int(x),int(y)))
        elif line.startswith('fold'):
            result = re.search(r"(x|y)=(\d+)", line)
            folds.append((result.group(1), int(result.group(2))))

    for (fold_direction, fold_value) in folds:
        if fold_direction == 'x':
            points = fold_x(points, fold_value)
        else:
            points = fold_y(points, fold_value)

    results = [['X' if (x,y) in points else ' ' for x in range(40)] for y in range(6)]
    for row in results:
        print(''.join(row))

