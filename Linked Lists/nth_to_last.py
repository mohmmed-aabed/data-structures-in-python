class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

# --------------------


def nth_to_last(step, head):
    left_marker = right_marker = head

    i = 0
    while i < (step - 1):
        if right_marker.next_node:
            right_marker = right_marker.next_node
            i += 1
        else:
            raise LookupError('n is larger than the linked list')

    while right_marker.next_node:
        right_marker = right_marker.next_node
        left_marker = left_marker.next_node

    return left_marker.value


print(nth_to_last(2, a))
