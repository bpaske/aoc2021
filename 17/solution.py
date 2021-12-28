from itertools import count
from collections import Counter

y_min = -88
y_max = -142
x_min = 128
x_max =160

speeds = set()
for initial_y_speed in range(-150,150):
    for initial_x_speed in range(1,161):
        x = 0
        y = 0
        x_speed = initial_x_speed
        y_speed = initial_y_speed
        for r in count(1):
            #print(x, y, x_speed, y_speed, t)
            if x >= x_min and x <= x_max and y<= y_min and y >= y_max:
                speeds.add((initial_x_speed, initial_y_speed))
                break
            elif x > x_max or y < y_max or (x_speed == 0 and x < x_min):
                break
            else:
                x += x_speed
                y += y_speed
                x_speed -= 1
                x_speed = max(0, x_speed)
                y_speed -= 1

print(len(speeds))

