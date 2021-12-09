with open('./input.txt') as f:
    numbers=[[int(n) for n in l.strip()] for l in f.readlines()]

    risk = 0
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
                risk+= 1 + number

    print(risk)
