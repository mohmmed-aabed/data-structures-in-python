class Node:

    def __init__(self, value):
        self.value = value
        self.next_node = None


a = Node(10)
b = Node(20)
c = Node(30)

a.next_node = b
b.next_node = c

print(a.next_node.value)
print(b.next_node.value)
