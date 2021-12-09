from math import floor
from statistics import mean
with open('./input.txt') as f:
    numbers = [int(x) for x in f.readline().strip().split(',')]
    max_number = max(numbers)

    print(min(sum((abs(x - y)*(abs(x-y)+1))/2 for x in numbers) for y in range(max_number)))
