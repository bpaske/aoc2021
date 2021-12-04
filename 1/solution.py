with open('./input.txt') as f:
    increasing = 0
    numbers = [int(l) for l in f.readlines()]
    for i in range(1,len(numbers)):
        if numbers[i] > numbers[i-1]:
            increasing +=1
    print(increasing)
