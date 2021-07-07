"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

def move_zeros(array):
    # function takes an array and moves all of the zeros to the end, preserving the order of the other elements

    shift = 0 # stores amount of encountered zeroes in the array
    for idx, val in enumerate(array):
        if val == 0:
            # zero is encountered
            shift += 1
        if shift and val != 0:
            # there is at least one zero in the array (if false there is no need to change order in the array) and the current value is nonzero (so that shift amount is correct)
            # place nonzero element shifted to the left by shift amount
            array[idx - shift] = val
    
    for i in range(shift):
        # place shift amount of zeroes at the end of the array
        array[-(i+1)] = 0

    return array
