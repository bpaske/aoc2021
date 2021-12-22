import re

cubes = {}
on = 'on'
off = 'off'


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

        # print(f"({x1}, {x2}), ({y1}, {y2}), ({z1}, {z2}), {on_or_off}")

        for x in range(max(min(x1, x2), -50), min(max(x1, x2),50)+1, 1):
            for y in range(max(min(y1, y2), -50), min(max(y1, y2),50)+1, 1):
                for z in range(max(min(z1, z2), -50), min(max(z1, z2),50)+1, 1):
                    cubes[(x,y,z)] = True if  on_or_off == on else False
print(sum(1 for k in cubes.values() if k))
