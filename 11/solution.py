from octopus import Octopus, read_octopuses

def part1(octopuses):
    minx = 0
    miny = 0
    maxx = len(octopuses[0])
    maxy = len(octopuses)

    flash_count = 0
    for _ in range(100):
        for octopusrow in octopuses:
            for octopus in octopusrow:
                octopus.increment_energy()

        flashed = True
        while flashed:
            flashed = False
            for y, octopusrow in enumerate(octopuses):
                for x, octopus in enumerate(octopusrow):
                    if octopus.flash_if_possible():
                        flashed = True
                        flash_count += 1
                        for (j, i) in [ (j, i) for j in range(y-1, y+2) for i in range(x-1, x+2) if j >= miny and i >= minx and j < maxy and i <maxx]:
                            octopuses[j][i].increment_energy()

        for octopusrow in octopuses:
            for octopus in octopusrow:
                octopus.reset()

    return flash_count

def part2(octopuses):
    minx = 0
    miny = 0
    maxx = len(octopuses[0])
    maxy = len(octopuses)

    run =1
    while True:
        for octopusrow in octopuses:
            for octopus in octopusrow:
                octopus.increment_energy()
        flashed = True
        while flashed:
            flashed = False
            for y, octopusrow in enumerate(octopuses):
                for x, octopus in enumerate(octopusrow):
                    if octopus.flash_if_possible():
                        flashed = True
                        for (j, i) in [ (j, i) for j in range(y-1, y+2) for i in range(x-1, x+2) if j >= miny and i >= minx and j < maxy and i <maxx]:
                            octopuses[j][i].increment_energy()
        all_flashed = all( o.flashed  for r in octopuses for o in r)
        if all_flashed:
            return run


        for octopusrow in octopuses:
            for octopus in octopusrow:
                octopus.reset()
        run +=1

octopuses = read_octopuses('./input.txt')
print(part1(octopuses))
octopuses = read_octopuses('./input.txt')
print(part2(octopuses))
