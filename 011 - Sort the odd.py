"""
You will be given an array of numbers.
You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples

[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""


def sort_array(source_array):
    """function sorts odd numbers from source_array in ascending order while leaving even numbers as they were"""
    
    odds = []

    # res retains even values as they were in source_array and None insdead of odd values
    # odd values added to odds as a tuple: (index, value in a given index)
    res = [source_array[idx] if (source_array[idx] % 2 == 0) else odds.append((idx,source_array[idx])) for idx in range(len(source_array))]
   
    # sort odds by value (by second element in a tuple)
    odds.sort(key=lambda elem: elem[1])

    # replace tuple with values only
    sorted_odd_values = [odd_val[1] for odd_val in odds]

    # add ordered odd values in a place of None values to the result array 
    j = 0
    for i in range(len(source_array)):
        if res[i] == None:
            res[i] = sorted_odd_values[j]
            j += 1

    return res


print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
