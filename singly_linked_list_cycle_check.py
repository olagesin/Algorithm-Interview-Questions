"""
Problem: Check if a Linked list is circular. i.e if the last node in a linked list connects to the first node
"""


class Node:
    def __init__(self, data = None):
        self.data = data
        self.nextnode = None


def cycle_check(node):
    marker1 = node
    marker2 = node

    while marker2 is not None and marker2.nextnode is not None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker2 == marker1:
            return True

    return False


a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a #Cycle Linked List


x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z

print(cycle_check(x))
