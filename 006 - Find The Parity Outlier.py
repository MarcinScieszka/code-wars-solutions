"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.

Examples:

[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""

def find_outlier(integers):
    res_0 = integers[0] % 2
    res_1 = integers[1] % 2
    res_2 = integers[2] % 2

    # determining array type: if two values from the first three elements of integers of the integers array are even that means that whole array is mostly even
    if (res_0 == 0 and res_1 == 0) or (res_1 == 0 and res_2 == 0) or (res_0 == 0 and res_2 == 0):
        array_type = 1 # array contains mostly even numbers
    else:
        array_type = 0 # array contains mostly odd numbers
    
    # finding outlier in integers array based on type of array:
    for value in integers:
        if value % 2 == array_type:
            return value
 