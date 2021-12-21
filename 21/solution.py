from itertools import cycle, islice
player1_position = 4
player2_position = 6

player1_score = 0
player2_score = 0

dice = cycle(range(1, 101))
dice_rolls = 0
while True:
    print(f"Player 1: {player1_position}, {player1_score}\nPlayer 2: {player2_position}, {player2_score}")
    player1_roll_sum = sum(islice(dice, 3))
    dice_rolls +=3
    player1_position = (player1_position + player1_roll_sum) % 10
    player1_score += (player1_position ) if player1_position != 0 else 10

    if player1_score >= 1000:
        break

    player2_roll_sum = sum(islice(dice, 3))
    dice_rolls +=3
    player2_position = (player2_position + player2_roll_sum) % 10
    player2_score += (player2_position ) if player2_position !=0 else 10

    if player2_score >= 1000:
        break
answer = (dice_rolls *player2_score) if player1_score >= 1000 else (dice_rolls * player1_score)
print(answer)
