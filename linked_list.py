class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next is not None:
            total += 1
            current = current.next
        return total

    def display(self):
        elements = []
        current = self.head

        while current.next is not None:
            current = current.next
            elements.append(current.data)
        print(elements)


my_list = LinkedList()

my_list.display()

my_list.append(12)
my_list.append(34)
# my_list.append(45)
#
# my_list.display()
