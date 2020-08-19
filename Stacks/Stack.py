class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


stack = Stack()
print(stack.is_empty())

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.size())
