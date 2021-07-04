"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should return 6 - [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum.
Note that the empty list or array is also a valid sublist/subarray.
"""

def max_sequence(arr):
    has_positive_value = False
    has_negative_value = False
    array_length = len(arr)
    max_sum = 0

    if array_length == 0:
        # list is empty
        return 0

    for val in arr:
        if val >= 0:
            has_positive_value = True
        else:
            has_negative_value = True
            
        if has_positive_value and has_negative_value:
            # list is made up of both positive and negative numbers
            break

    if has_positive_value and not has_negative_value:
        # list is made up of only positive numbers
        return sum(arr)
    elif not has_positive_value and has_negative_value:
        # list is made up of only negative numbers
        return 0

    # sum values from arrays arranged in sequences: one array of size len(arr), two arrays of size len(arr) - 1, ..., len(arr) arrays of size 1
    # therefore, there will be len(arr) many lengths of arrays
    for i in range(array_length):
        for j in range(i+1):
            currnet_sum = sum(arr[0+j:array_length-(i-j)])
            # print(arr[0+j:array_length-(i-j)]) # visualisation of considered sequences
            if currnet_sum > max_sum:
                # new max sum has been found
                max_sum = currnet_sum
    
    return max_sum

# print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # returns sum([4, -1, 2, 1])
print(max_sequence([0, -1, 2, -3, 4, -5])) # returns sum([4])
# print(max_sequence([])) # empty list
# print(max_sequence([-1, -4, -3])) # only negative values
# print(max_sequence([1, 4, 3])) # only positive values
