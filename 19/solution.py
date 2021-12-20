from collections import defaultdict
import re

def substract_points(p1, p2):
    (x1,y1,z1) = p1
    (x2,y2,z2) = p2
    return x1-x2, y1 - y2, z1 - z2

def abs_point(p):
    x, y, z = p
    return abs(x), abs(y), abs(x)

def generate_rotation(p, i):
    x, y, z = p
    rotations = [(x,y,z),         (x, -1*y, -1*z), (x, z, -1*y), (x, -1*z, y),
                 (-1*x, y, -1*z), (-1*x, -1*y, z), (-1*x, z, y), (-1*x, -1*z, -1*y ),
                 (y, x,-1*z), (y, -1*x, z ), (y, z, x), (y, -1*z,-1*x),
                 (-1*y, x, z), (-1*y, -1*x, -1*z ), (-1*y, z,-1*x), (-1*y, -1*z, x ),
                 (z, x, y), (z, -1*x, -1*y), (z, y, -1*x), (z, -1*y, x),
                 (-1*z, x, -1*y), (-1*z, -1*x, y ), (-1*z, y, x), (-1*z, -1*y, -1*x)]
    return rotations[i]

scanner_points = defaultdict(list)
with open('./input.txt') as f:
    current_scanner=0
    for l in f.readlines():
        match = re.match(r"--- scanner (\d+) ---", l)
        if match:
            current_scanner = int(match.group(1))
        else:
            if l.strip():
                scanner_points[current_scanner].append(tuple(int(i) for i in l.strip().split(',')))

points_relative_to_scanner_0 = { 0: scanner_points[0] }
offsets = {0: (0,0,0)}

#Grim from performance point of view should the relative distances for each combination outside of the loop
while sorted(scanner_points.keys()) != sorted(points_relative_to_scanner_0.keys()):
    for s in [ sp for sp in scanner_points if sp not in points_relative_to_scanner_0]:
        for t, points in points_relative_to_scanner_0.copy().items():
            for (o0, o1, rotation) in ((p0, p1, i) for p0 in points for p1 in scanner_points[s] for i in range(24)):
                relative_0_points = { substract_points(p0, o0): p0 for p0 in points}
                rotated_origin = generate_rotation(o1, rotation)
                relative_1_points = { substract_points(generate_rotation(p1,rotation), rotated_origin): p1 for p1 in scanner_points[s] }

                relative_points_in_common = set(relative_0_points.keys()) & set( relative_1_points.keys())
                if len(relative_points_in_common) >= 12:
                    first_common_point = next(iter(relative_points_in_common))
                    offset = substract_points(generate_rotation(relative_1_points[first_common_point], rotation), relative_0_points[first_common_point])
                    offsets[s]=offset
                    points_relative_to_scanner_0[s] = [substract_points(generate_rotation(p, rotation), offset) for p in scanner_points[s]]
                    break

print(offsets)
print(len(set(l for v in points_relative_to_scanner_0.values() for l in v)))
differences = [[abs(x1-x2), abs(y1 -y2), abs(z1-z2)] for x1, y1, z1 in offsets.values() for x2, y2, z2 in offsets.values()]
print(max(sum(d) for d in differences))
