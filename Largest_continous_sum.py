"""
Code Objective: Given an array of numbers, find the largest continuous sum
"""


def sum_largest_cont(arr):
    if len(arr) == 0:
        return 0
    else:
        current_sum = max_sum = arr[0]
        for number in arr[1:]:

            current_sum = max(current_sum + number, number)

            max_sum = max(current_sum, max_sum)

        return max_sum


print(sum_largest_cont([1, 2, -1, 3, 4,  10, 10, -10, 1]))
