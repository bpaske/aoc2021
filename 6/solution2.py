from functools import cache

@cache
def calculate_total(start, internal_timer):
    if start -internal_timer <= 0:
        return 0
    else:
        return 1 + calculate_total(start-internal_timer-1, 6) + calculate_total(start - internal_timer -1, 8)

with open('./input.txt') as f:
    initial_values = (int(x) for x in f.readline().split(','))
    total = sum((1 + calculate_total(256, x)) for x in initial_values)
    print(total)
