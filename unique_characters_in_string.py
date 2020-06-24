"""
Problem: Given a string s, determine if it comprises of all unique elements
for example: the string 'abcde' comprises of all unique elements while the string 'aabde'
doesn't.
There are two different methods used here
"""


def unique(test_string):
    container = set()
    for i in range(len(test_string)):
        if test_string[i] not in container:
            container.add(test_string[i])
        else:
            return False
    return True


def unique_(test_string):
    return len(set(test_string)) == len(test_string)


print(unique("abcdea"))
print(unique_("abcdea"))

print(unique("abcde"))
print(unique_("abcde"))
