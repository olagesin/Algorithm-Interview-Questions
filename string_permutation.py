"""
Write a function that takes a string and recursively returns a list of permutations
E.G for the string 'abc',
the output should return
['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

you get?
"""


def permute(input_string):
    output = []

    if len(input_string) == 1:
        output = [input_string]
        print("output value 1 is {0}" .format(output))
    else:
        for i, letter in enumerate(input_string):
            print("letter is {0}" .format(letter))
            for perm in permute(input_string[:i] + input_string[i+1:]):
                print("Other letter is  {0}" .format(letter))
                print("perm is {0}" .format(perm))
                output += [letter + perm]
                print("output is {0}" .format(output))

    return output


value = permute('abc')
print(value)
