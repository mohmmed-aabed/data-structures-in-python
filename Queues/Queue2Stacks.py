class Queue2Stacks:

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, item):
        self.instack.append(item)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()


queue = Queue2Stacks()

for i in range(10):
    queue.enqueue(i)

for i in range(10):
    print(queue.dequeue())
