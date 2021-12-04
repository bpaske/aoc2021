with open('./input.txt') as f:
    increasing = 0
    numbers = [int(l) for l in f.readlines()]
    for i in range(4,len(numbers)+1):
        if sum(numbers[i-3:i]) > sum(numbers[i-4:i-1]):
            increasing +=1
    print(increasing)
