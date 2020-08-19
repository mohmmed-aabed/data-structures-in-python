class Node:

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None


a = Node(100)
b = Node(200)
c = Node(300)

a.next_node = b
b.prev_node = a

b.next_node = c
c.prev_node = b

print(b.next_node.value)
print(b.prev_node.value)
