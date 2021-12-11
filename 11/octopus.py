class Octopus:
    def __init__(self, energy):
        self.energy = energy
        self.flashed = False

    def increment_energy(self):
        self.energy += 1

    def flash_if_possible(self):
        if not self.flashed and self.energy > 9:
            self.flashed = True
            return True
        else:
            return False

    def reset(self):
        if(self.flashed):
            self.flashed = False
            self.energy = 0

def read_octopuses(file):
    with open('./input.txt') as f:
        octopuses = [[Octopus(int(i)) for i in line.strip()] for line in f.readlines()]
        return octopuses
