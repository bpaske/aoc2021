import re
from itertools import cycle

cubes = []
on = 'on'
off = 'off'

def find_overlapping_cube(c1, c2):
    ((x1min, x1max), (y1min, y1max), (z1min, z1max)) = c1
    ((x2min, x2max), (y2min, y2max), (z2min, z2max)) = c2

    if x1min <= x2max and x1max >= x2min and y1min <= y2max and y1max >= y2min and z1min <= z2max and z1max >= z2min:
        return ((max(x1min, x2min), min(x1max, x2max)), (max(y1min, y2min), min(y1max, y2max)), (max(z1min, z2min), min(z1max, z2max)))

    return None

def calculate_area_of_cube(c):
    ((x1,x2), (y1, y2), (z1, z2)) = c
    return (x2+1-x1)*(y2+1-y1)*(z2+1-z1)

with open('./input.txt') as f:
    for l in f.readlines():
        match = re.match(r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", l)
        if not match:
            print(f"Failed to parse: {l}")
            exit(1)
        on_or_off = match.group(1)
        x1 = int(match.group(2))
        x2 = int(match.group(3))
        y1 = int(match.group(4))
        y2 = int(match.group(5))
        z1 = int(match.group(6))
        z2 = int(match.group(7))

        cubes.append(((min(x1,x2), max(x1,x2)), (min(y1,y2), max(y1,y2)), (min(z1,z2), max(z1,z2)), on_or_off))


total_intersecting_volume = sum(calculate_area_of_cube(v[:3]) for v in cubes if v[3] == on)
intersecting_areas_previous_length = {(i,): values[:3] for i, values in enumerate(cubes) if values[3] == on}

even_cycle = cycle([True, False])
while len(intersecting_areas_previous_length) > 0:
    next_intersection_areas = {}
    volume_total= 0
    for k, current_cube in intersecting_areas_previous_length.items():
        last_index = k[-1]
        for h, next_cube in enumerate(cubes[last_index+1:]):
            i = last_index+1+h
            overlapping_cube = find_overlapping_cube(current_cube, next_cube[:3])
            if overlapping_cube:
                volume_total += calculate_area_of_cube(overlapping_cube)
                next_intersection_areas[k +(i,)] = overlapping_cube
    intersecting_areas_previous_length = next_intersection_areas
    total_intersecting_volume = (total_intersecting_volume - volume_total) if next(even_cycle) else (total_intersecting_volume + volume_total)

print(total_intersecting_volume)

