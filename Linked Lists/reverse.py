class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next_node = b
b.next_node = c
c.next_node = d

print(a.next_node.value)
print(b.next_node.value)
print(c.next_node.value)

# --------------------


def reverse(head):

    current = head
    previous = None
    nextnode = None

    while current:
        nextnode = current.next_node
        current.next_node = previous
        previous = current
        current = nextnode

    return previous


reverse(a)

print(d.next_node.value)
print(c.next_node.value)
print(b.next_node.value)
