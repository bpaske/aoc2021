import re

grid = []

for x in range(1000):
    grid.append([0]*1000)

with open('./input.txt') as f:
    for line in f.readlines():
        [x1, y1, x2, y2] = [int(i) for i in re.findall(r'\d+', line)]

        if x1 == x2:
            if y1<y2:
                for y in range(y1, y2+1):
                    grid[y][x1] +=1
            else:
                for y in range(y2, y1+1):
                    grid[y][x1] +=1
        elif y1 == y2:
            if x1 < x2:
                for x in range(x1, x2+1):
                    grid[y1][x] +=1
            else:
                for x in range(x2, x1+1):
                    grid[y1][x] +=1
        else:
            if x1 < x2 and y1 < y2:
                for i in range(x2-x1+1):
                    grid[y1+i][x1+i] +=1
            elif x1 >= x2 and y1 >= y2:
                for i in range(x1-x2+1):
                    grid[y2+i][x2+i] +=1
            elif x1 < x2 and y1>=y2:
                for i in range(x2-x1+1):
                    grid[y1-i][x1+i] +=1
            elif x1 >= x2 and y1<y2:
                for i in range(x1-x2+1):
                    grid[y1+i][x1-i] +=1
            else:
                print(x1, y1, x2, y2)
                exit(1)

print(len([i for row in grid for i in row if i >1]))
