class LaternFish:
    def __init__(self, timer):
        self.timer = timer
    def generateNextDayData(self):
        if self.timer == 0:
            return [LaternFish(6), LaternFish(8)]
        else:
            return[LaternFish(self.timer -1)]

with open('./input.txt') as f:

    laternfishes = [LaternFish(int(x)) for x in f.readline().split(',')]
    for i in range(80):
        laternfishes = [l for old_laternfishes in laternfishes for l in old_laternfishes.generateNextDayData()]
    print(len(laternfishes))
