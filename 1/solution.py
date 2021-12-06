with open('./input.txt') as f:
    increasing = 0
    numbers = [int(l) for l in f.readlines()]
    for i in range(1,len(numbers)):
        if numbers[i] > numbers[i-1]:
            increasing +=1

    print(sum(1 for (first, second) in zip(numbers[0:-1], numbers[1:]) if second > first))
    alt_increaing = sum((1 if value> numbers[index] else 0 for (index, value) in enumerate(numbers[1:])  ))
    print(alt_increaing)
    print(increasing)
