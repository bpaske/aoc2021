from collections import Counter
from functools import cache

roll_frequencies = Counter(a+b+c for a in range(1,4) for b in range(1,4) for c in range(1,4))

@cache
def calculate_wins(game_state):
    (player1_position, player1_score, player2_position, player2_score) = game_state

    if player2_score >= 21:
        return 0, 1

    player1_wins = 0
    player2_wins = 0

    for roll, roll_count in roll_frequencies.items():
        new_position = (player1_position + roll) % 10
        new_score = ( player1_score + new_position ) if new_position !=0 else (player1_score + 10)
        next_state = ( player2_position, player2_score, new_position, new_score)

        additional_player2_wins, additional_player1_wins = calculate_wins(next_state)
        player1_wins += roll_count*additional_player1_wins
        player2_wins += roll_count*additional_player2_wins

    return player1_wins, player2_wins

print(calculate_wins((4,0,8,0)))
