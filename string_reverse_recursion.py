"""
Write a function to reverse a string using Recursion
"""


def reverse(phrase):
    if len(phrase) == 1:
        return phrase
    else:
        return reverse(phrase[1:]) + phrase[0]


print(reverse("Helloiuyte"))
