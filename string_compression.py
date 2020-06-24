"""
    Program to compress strings in python
    e.g: given a string AAABB, the output should read: A3B2
"""


def compress(test_string):
    result = ""
    count = 1
    i = 1
    while i < len(test_string):
        if test_string[i] == test_string[i - 1]:
            count += 1
        else:
            result += test_string[i - 1] + str(count)
            count = 1

        i += 1

    result += test_string[i - 1] + str(count)
    return result


print(compress("AAABccvCC"))
print(compress("A"))
print(compress("AAABBBCC"))
print(compress("AAABBBERRR"))