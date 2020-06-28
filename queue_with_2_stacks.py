"""
problem: Create a Queue data structure using two stacks
"""


class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)]

    def size(self):
        return len(self.items)


class Queue(object):

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def isEmpty(self):
        return self.stack1.size() == 0

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack1.size() == 0:
            return self.stack1
        else:
            for i in range(self.stack1.size()):
                self.stack2.push(self.stack1.pop())

            temp = self.stack2.pop()

            for i in range(self.stack2.size()):
                self.stack1.push(self.stack2.pop())

        return temp

    def size(self):
        return self.stack1.size()


queue = Queue()

for i in range(5):
    queue.enqueue(i)

for i in range(5):
    print(queue.dequeue())
# print(queue.isEmpty())
# queue.enqueue("saml")
# queue.enqueue("oll")
# print(queue.isEmpty())
# print(queue.size())
# queue.dequeue()
# print(queue.size())
