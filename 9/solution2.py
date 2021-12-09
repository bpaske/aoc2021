def find_size_of_basin(numbers, starting_index):
    visited_indexes = set()
    to_visit_indexes = [starting_index]

    while len(to_visit_indexes) > 0:
        current_index = to_visit_indexes.pop()
        visited_indexes.add(current_index)
        i,j = current_index
        if i > 0:
            candidate = numbers[i-1][j]
            if candidate !=9 and (i-1,j) not in visited_indexes:
                to_visit_indexes.append((i-1,j))
        if i< number_of_rows-1:
            candidate = numbers[i+1][j]
            if candidate !=9 and (i+1,j) not in visited_indexes:
                to_visit_indexes.append((i+1,j))
        if j > 0:
            candidate = numbers[i][j-1]
            if candidate !=9 and (i,j-1) not in visited_indexes:
                to_visit_indexes.append((i,j-1))
        if j< number_of_columns-1:
            candidate = numbers[i][j+1]
            if candidate !=9 and (i,j+1) not in visited_indexes:
                to_visit_indexes.append((i,j+1))

    return len(visited_indexes)

with open('./input.txt') as f:
    numbers=[[int(n) for n in l.strip()] for l in f.readlines()]

    low_points =[]
    number_of_rows = len(numbers)
    number_of_columns = len(numbers[0])
    for i, row in enumerate(numbers):
        for j, number in enumerate(row):
            numbers_to_compare = []
            if i > 0:
                numbers_to_compare.append(numbers[i-1][j])
            if i< number_of_rows-1:
                numbers_to_compare.append(numbers[i+1][j])
            if j > 0:
                numbers_to_compare.append(numbers[i][j-1])
            if j< number_of_columns-1:
                numbers_to_compare.append(numbers[i][j+1])
            if all(number < n for n in numbers_to_compare):
                low_points.append((i,j))

    basin_sizes = [ find_size_of_basin(numbers, lp) for lp in low_points]
    top_three = [x for x in sorted(basin_sizes, reverse=True)[:3]]
    print(top_three[0]*top_three[1]*top_three[2])
