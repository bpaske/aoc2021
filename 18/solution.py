def split_first(node, depth=1):
    if isinstance(node, int):
       return node, False, None, None

    [left, right] = node
    if depth < 4:
        new_left, changed, left_addition, right_addition = split_first(left, depth+1)
        if changed:
            if right_addition:
                right = update_leftmost_element(right, right_addition)
            return [new_left, right], True, left_addition, None
        else:
            new_right, changed, left_addition, right_addition = split_first(right, depth+1)
            if left_addition:
                new_left = update_rightmost_element(new_left, left_addition)
            return [new_left, new_right], changed, None, right_addition
    else:
       if isinstance(left, list):
           return[0,update_leftmost_element(right, left[1])], True, left[0], None
       elif isinstance(right, list):
            return [update_rightmost_element(left, right[0]), 0], True, None, right[1]
       else:
           return [left, right], False, None, None

def explode_first(node):
    if isinstance(node, int):
       return (node, False) if node <10 else([node//2, node-(node//2)], True)
    else:
        [left, right] = node
        new_left, changed = explode_first(left)
        if changed:
            return [new_left, right], True
        else:
            new_right, changed = explode_first(right)
            return [new_left, new_right], changed

def reduce(tree):
    changed = True
    current_tree = tree
    while changed:
        current_tree, changed,_,_ = split_first(current_tree)
        if not changed:
            current_tree, changed = explode_first(current_tree)
    return current_tree

def update_leftmost_element(tree, newvalue):
    if isinstance(tree, int):
        return tree + newvalue
    else:
        left, right = tree
        return [update_leftmost_element(left, newvalue), right]

def update_rightmost_element(tree, newvalue):
    if isinstance(tree, int):
        return tree + newvalue
    else:
        left, right = tree
        return [left, update_rightmost_element(right, newvalue)]

def magnitude(tree):
    if isinstance(tree, int):
        return tree
    else:
        [left, right] = tree
        return 3*magnitude(left) + 2*magnitude(right)

print(reduce([[[[[9,8],1],2],3],4]))

with open('./input.txt') as f:
    lines = [eval(l) for l in f.readlines()]
    current_line = lines[0]
    for l in lines[1:]:
        current_line = reduce([current_line, l])
    print(current_line)
    print(magnitude(current_line))


    print(max([magnitude(reduce([l,m])) for l in lines for m in lines]))
