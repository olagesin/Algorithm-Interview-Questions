"""
    Problem: Consider a non negative integer array, a new array is fromed by shuffling the elements of the
    first array and deleting a random number. Your job is to find the missing number from the list of new array
    Here we go, note: this is written to have a time complexity of O(n)
"""


def finder(first_array, second_array):
    setList = set(first_array)
    for element in setList:
        if first_array.count(element) == second_array.count(element):
            continue
        else:
            return element


arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [5, 4, 7, 1, 3, 6]
print(finder(arr1, arr2))
