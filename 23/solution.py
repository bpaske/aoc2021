import copy
from heapq import heappop, heappush
import math

costs_per_move = {'A': 1, 'B': 10, 'C':100, 'D':1000}
initial_state = [[],[],['B','D', 'D', 'D'], [], ['D','B', 'C', 'B'], [], ['A', 'A', 'B', 'A'],[], ['C','C','A', 'C'], [],[]]

cave_indices = [2,4,6,8]
cave_index_to_letter = dict(zip(cave_indices, ['A','B','C','D']))
cave_letter_to_index = dict(zip(['A','B','C','D'], cave_indices))
hall_indices = [0,1,3,5,7,9,10]


def generate_next_states_and_cost(game_state):
    next_states = []
    for i, slot in enumerate(game_state):
        if len(slot) > 0:
            # Move any amphipod to destination cave if possible
            amphipod_type = slot[-1]
            home_cave_index = cave_letter_to_index[amphipod_type]
            if home_cave_index != i:
                home_cave = game_state[home_cave_index]
                if all(h == amphipod_type for h in home_cave):
                    if i < home_cave_index:
                        if all(len(game_state[k]) == 0 for k in range(i+1, home_cave_index) if k in hall_indices):
                               next_state = copy.deepcopy(game_state)
                               next_state[home_cave_index].append(next_state[i].pop())
                               # Distinguish between cave and non-cave distances
                               distance = home_cave_index-i  + 4 - len(game_state[home_cave_index])
                               if i in cave_indices:
                                   distance += 5 - len(game_state[i])
                               next_states.append((next_state, distance * costs_per_move[amphipod_type]))
                               return next_states
                    if i > home_cave_index:
                        if all(len(game_state[k]) == 0 for k in range(home_cave_index +1, i) if k in hall_indices):
                               next_state = copy.deepcopy(game_state)
                               next_state[home_cave_index].append(next_state[i].pop())
                               # Distinguish between cave and non-cave distances
                               distance = i - home_cave_index  + 4 - len(game_state[home_cave_index])
                               if i in cave_indices:
                                   distance += 5 - len(game_state[i])
                               next_states.append((next_state, distance * costs_per_move[amphipod_type]))
                               return next_states

            if i in cave_indices and not all(c == cave_index_to_letter[i] for c in slot):
                #Go rightwards
                for j in [x for x in hall_indices if x > i]:
                    if len(game_state[j]) < 1:
                        next_state = copy.deepcopy(game_state)
                        amphipod_type = next_state[i].pop()
                        next_state[j].append(amphipod_type)
                        next_states.append((next_state, (5 - len(game_state[i]) + j - i )* costs_per_move[amphipod_type]))
                    else:
                        break
                #Go leftwards
                for j in [x for x in reversed(hall_indices) if x < i]:
                    if len(game_state[j]) < 1:
                        next_state = copy.deepcopy(game_state)
                        amphipod_type = next_state[i].pop()
                        next_state[j].append(amphipod_type)
                        next_states.append((next_state, (5 - len(game_state[i]) + i - j ) * costs_per_move[amphipod_type]))
                    else:
                        break
    return next_states


def has_won(state):
    return all( state[i] == [c,c,c,c]  for (i,c) in zip(cave_indices, ['A', 'B', 'C', 'D']))

def min_bound_weight(state):
    min_bound_weight = 0
    for i, slot in enumerate(state):
        for j, element in enumerate(slot):
            home_cave_index = cave_letter_to_index[element]
            min_bound_weight += (abs(i - home_cave_index) + 1) * costs_per_move[element] if i in hall_indices else (abs(j - home_cave_index) + 5 - j) * costs_per_move[element]
    return min_bound_weight

def find_cheapest_cost(state, bound):
    if has_won(state):
        print('found solution')
        return 0
    next_states = generate_next_states_and_cost(state)
    min_cost = bound

    for state, cost in next_states:
        if min_cost - cost > 0:
            total_cost = find_cheapest_cost(state, min_cost-cost) + cost
            if total_cost < min_cost:
                min_cost = total_cost
    return min_cost

print(find_cheapest_cost(initial_state, math.inf))

#results = generate_next_states_and_cost(initial_state)
#results = generate_next_states_and_cost([[], [], ['A', 'B'], ['B'], ['D', 'C'], [], ['C'], [], ['A', 'D'], [], []])
#print(generate_next_states_and_cost([[],[],['A'], [], ['B', 'B'], [], ['C', 'C'],[], ['D', 'D'], ['A'],[]]))
#print(generate_next_states_and_cost([[],[],['A'], [], ['B', 'B'], ['D'], ['C', 'C'],['D'], [], ['A'],[]]))
#print(generate_next_states_and_cost([[], [], ['A'], [], ['B', 'B'], ['D'], ['C', 'C'], [], ['D'], ['A'], []]))
