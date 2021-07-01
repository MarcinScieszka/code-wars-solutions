"""
"Multiples of 3 or 5"

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note:   
    If the number is a multiple of both 3 and 5, only count it once. 
    Also, if a number is negative, return 0(for languages that do have them)
"""


def solution_0(number):
    if number < 0:
        return 0
    sum = 0
    for i in range (0, number):
        if (i % 3 == 0 and i % 5 == 0) or i % 3 == 0 or i % 5 == 0:
            sum += i
            
    return sum

def solution_1(number):
    if number <= 0:
        return 0
    
    sum = 0
    num = (number - 1)  # max used number
    
    num_of_fives = num // 5
    num_of_threes = num // 3
    num_of_fifteens = num // 15

    curr_mul_of_threes = 0
    curr_mul_of_fives = 0
    curr_mul_of_fifteens = 0
    
    # remove duplicated values
    for i in range(0, num_of_fifteens):
        curr_mul_of_fifteens += 15
        sum -= curr_mul_of_fifteens
    
    # add multiples of 3
    for i in range(0, num_of_threes):
        curr_mul_of_threes += 3
        sum += curr_mul_of_threes

    # add multiples of 5
    for i in range(0, num_of_fives):
        curr_mul_of_fives += 5
        sum += curr_mul_of_fives

    return sum