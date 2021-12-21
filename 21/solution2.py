from collections import Counter
from itertools import cycle

universes = Counter()
universes[(4,0,6,0)] =1
roll_frequencies = Counter(a+b+c for a in range(1,4) for b in range(1,4) for c in range(1,4))

player1_wins = 0
player2_wins = 0

player1_turn_cycle = cycle([True, False])

while sum(universes.values()) > 0:
    new_universes = Counter()
    is_player1_turn = next(player1_turn_cycle)
    for (player1_position, player1_score, player2_position, player2_score), number_of_universes in universes.items():
        for roll, roll_count in roll_frequencies.items():
            if is_player1_turn:
                new_position = (player1_position + roll) % 10
                new_score = ( player1_score + new_position ) if new_position !=0 else (player1_score + 10)
                if new_score >=21:
                    player1_wins += number_of_universes * roll_count
                else:
                    new_universes[(new_position, new_score, player2_position, player2_score)] += number_of_universes * roll_count
            else:
                new_position = (player2_position + roll) % 10
                new_score = ( player2_score + new_position ) if new_position !=0 else (player2_score + 10)
                if new_score >=21:
                    player2_wins += number_of_universes * roll_count
                else:
                    new_universes[(player1_position, player1_score, new_position, new_score)] += number_of_universes * roll_count
    universes = new_universes

print(player1_wins)
print(player2_wins)
