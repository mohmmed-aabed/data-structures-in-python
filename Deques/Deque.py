class Deque:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


deque = Deque()
print(deque.is_empty())

deque.add_front(10)
deque.add_front(20)

deque.add_rear('A')
deque.add_rear('B')

print(deque.remove_front())
print(deque.remove_rear())
print(deque.size())
