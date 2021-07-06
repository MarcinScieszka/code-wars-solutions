"""
You will be given an array of numbers.
You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples

[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""


def sort_array(source_array):
    """function takes an array of numbers and sorts the odd numbers in ascending order while leaving the even numbers at their original positions"""
    
    odds = []

    # res replaces odd values (which are added to odds) with None and retains even values as they were in source_array 
    res = [val if (val % 2 == 0) else odds.append(val) for val in source_array]
   
    odds.sort()

    # replace None with ordered odd values
    odds_iter = iter(odds)
    for idx, val in enumerate(res):
        if val == None:
            res[idx] = next(odds_iter)

    return res


print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
