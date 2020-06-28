"""
Problem: write a function that checks if an input parenthesis is balanced
for example, the string '()' is a balanced parenthesis while '(()' is not
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


def balance_check(test_string):
    if len(test_string) % 2 != 0:
        return False
    else:
        openings = set("({[")

        stack = Stack()

        matches = set([ ('(',')'), ('[',']'), ('{','}') ])

        for char in test_string:
            if char in openings:
                stack.push(char)
            else:
                if stack.size() == 0:
                    return False
                last_char = stack.pop()

                if (last_char, char) not in matches:
                    return False
        return stack.size() == 0


print(balance_check("(())[][()]"))
