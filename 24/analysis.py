with open('./input.txt') as f:
    instructions = f.readlines()
    for i in range(0,18):
        for j in range(0,14):
            print(instructions[j*18+i].strip())
        print('\n')

