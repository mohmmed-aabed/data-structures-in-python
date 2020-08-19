def binary_tree(r):
    return [r, [], []]


def insert_left(root, new_brance):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_brance, [], []])
    else:
        root.insert(1, [new_brance, t, []])
    return root


def insert_right(root, new_brance):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_brance, [], []])
    else:
        root.insert(2, [new_brance, [], t])
    return root


def get_root_value(root):
    return root[0]


def set_root_value(root, new_value):
    root[0] = new_value


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


r = binary_tree(3)

insert_left(r, 4)
insert_left(r, 5)
insert_right(r, 6)
insert_right(r, 7)

print(r)
# [3, [5, [], []], [7, [], []]]

left = get_left_child(r)
right = get_right_child(r)

print(left)
# [5, [], []]
print(right)
# [7, [], []]
