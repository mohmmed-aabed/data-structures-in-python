class Circular:

    def __init__(self, value):
        self.value = value
        self.next_node = None


a = Circular(10)
b = Circular(20)
c = Circular(30)

a.next_node = b
b.next_node = c
c.next_node = a

# --------------------


class Linear:

    def __init__(self, value):
        self.value = value
        self.next_node = None


x = Linear(100)
y = Linear(200)
z = Linear(300)

x.next_node = y
y.next_node = z

# --------------------


def cycle_check(head):

    marker1 = head
    marker2 = head

    while marker2 != None and marker2.next_node != None:
        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node

        if marker1 == marker2:
            return True

    return False


print(cycle_check(a))
print(cycle_check(x))
