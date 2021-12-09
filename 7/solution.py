from math import floor
with open('./input.txt') as f:
    numbers = sorted([int(x) for x in f.readline().strip().split(',')])
    midpoint = len(numbers)//2
    median = numbers[midpoint]

    print(sum(abs(x -median) for x in numbers))
