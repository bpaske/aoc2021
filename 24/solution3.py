from collections import defaultdict, Counter
from functools import cache
def run_cycle(a, b, c, d, e):
    w = a
    x = (b%26)
    z = b // c
    x += d
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 25
    y *=x
    y += 1
    z *= y
    y = a
    y += e
    y *= x
    z += y
    return z

def alt_run_cycle(a, b, c, d, e):
    if b%26 +d == a:
        return b //c
    else:
        return 26 * (b//c) + a +e

cs = [1, 1, 1, 26, 1, 1, 1, 26, 26, 1, 26, 26, 26, 26]
ds = [13, 11, 14, -5, 14, 10, 12, -14, -8, 13, 0, -5, -9, -1]
es = [0, 3, 8, 5, 13, 9, 6, 1, 1, 2, 7, 5, 8, 15]

# Initially did this analytically as it is possible to work out relationships between
# each of the inputs then coded this up after talking with G.
@cache
def search_for_solution(depth, previous_result):
    for a in range(9, 0 , -1):
        result = alt_run_cycle(a, previous_result, cs[depth], ds[depth], es[depth])
        if depth == 13 and result == 0:
            return a
        elif depth <13:
            result = search_for_solution(depth+1, result)
            if result:
                return f"{a}, {result}"
    return None
print (search_for_solution(0,0))



