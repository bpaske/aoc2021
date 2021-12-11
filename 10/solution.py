unmatched_costs = {')':3, ']':57, '}':1197, '>':25137}
closed_to_open_brackets={'}':'{', '>':'<', ')':'(', ']':'['}
open_to_closed_brackets ={v:k for k,v in closed_to_open_brackets.items()}
autocomplete_costs = {')':1, ']':2, '}':3, '>':4}
def find_autocomplete_costs(line):
    brackets = []
    for l in line:
        if l in closed_to_open_brackets:
            if brackets[-1] == closed_to_open_brackets[l]:
                brackets.pop()
            else:
                return 0
        else:
            brackets.append(l)
    autocomplete_brackets = [open_to_closed_brackets[l] for l in reversed(brackets)]
    cost = 0
    for a in autocomplete_brackets:
        cost = cost * 5 + autocomplete_costs[a]
    return cost

def find_unmatched_cost(line):
    brackets = []
    for l in line:
        if l in closed_to_open_brackets:
            if brackets[-1] == closed_to_open_brackets[l]:
                brackets.pop()
            else:
                return unmatched_costs[l]
        else:
            brackets.append(l)
    return 0

with open('./input.txt') as f:
    lines =[l.strip() for l in f.readlines()]
    print(sum( find_unmatched_cost(l) for l in lines ))
    costs = [find_autocomplete_costs(l) for l in lines]
    sorted_filtered_costs = sorted([c for c in costs if c !=0])
    print(sorted_filtered_costs[len(sorted_filtered_costs)//2])

