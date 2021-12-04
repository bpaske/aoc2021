class Board:
    def __init__(self, numbers,board_number, size=5):
        self.numbers = numbers
        self.size = size
        self.marked = []
        for i in range(size):
            self.marked.append ( [False]*5)
        self.board_number = board_number


    def add_number(self, number):
        for i in range(self.size):
            for j in range(self.size):
                if self.numbers[i][j] == number:
                    self.marked[i][j] = True

    def has_won(self):
        for x in range(self.size):
            if all(self.marked[x]):
                return True

        for j in range(self.size):
            column = [self.marked[i][j] for i in range(self.size)]
            if all(column):
                return True
        return False

    def display(self):
        print(self.board_number)
        print(self.numbers)
        print(self.marked)

    def sum_unmarked(self):
        sum = 0
        for i in range(self.size):
            for j in range(self.size):
                if not self.marked[i][j]:
                    sum += self.numbers[i][j]
        return sum




def create_board_from_lines(lines, board_number):
    numbers = [l.strip().split() for l in lines]
    for i in range(5):
        for j in range(5):
            numbers[i][j] = int(numbers[i][j])
    return Board(numbers, board_number)

with open('./input.txt') as f:
    lines = f.readlines()
    numbers_to_draw = [int(n) for n in lines[0].split(',')]
    boards = []
    boards_won = set()

    board_number = 1
    for i in range(2, len(lines), 6):
        boards.append(create_board_from_lines(lines[i: i+5], board_number))
        board_number +=1


    for n in numbers_to_draw:
        for b in boards:
            b.add_number(n)
            if b.has_won():
                boards_won.add(b.board_number)
                if len(boards_won) == 100:
                  print(b.sum_unmarked() * n)
                  exit()






