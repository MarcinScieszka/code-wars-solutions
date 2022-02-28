"""
Create a RomanNumerals class that can convert a roman numeral to and from an integer value. 
It should follow the API demonstrated in the examples below. 
Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting 
with the left most digit and skipping any digit with a value of zero. 
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 
2008 is written as 2000=MM, 8=VIII; or MMVIII. 
1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000

Symbol 	Value
I 	    1
IV 	    4
V 	    5
X 	    10
L 	    50
C 	    100
D 	    500
M 	    1000
"""

import string

class RomanNumerals:

    def to_roman(val: int) -> string:
        res = ''

        if (val > 4000):
            return

        thausands = (val // 1000 % 10)
        if thausands:
            res += thausands * 'M'
        
        hundreds = (val // 100 % 10)
        if hundreds:
            if (hundreds in [1, 2, 3]):
                res += hundreds * 'C'
            elif (hundreds == 4):
                res += 'CD'
            elif (hundreds == 5):
                res += 'D'
            elif (hundreds in [6, 7, 8]):
                res += ('D' + hundreds * 'C')
            elif (hundreds == 9):
                res += 'CM'
        
        tens = (val // 10 % 10)
        if tens:
            if (tens in [1, 2, 3]):
                res += (tens % 5) * 'X'
            elif (tens == 4):
                res += 'XL'
            elif (tens == 5):
                res += 'L'
            elif (tens in [6, 7, 8]):
                res += ('L' + (tens - 5) * 'X')
            elif (tens == 9):
                res += 'XC'

        ones = (val % 10)
        if ones:
            if (ones in [1, 2, 3]):
                res += (ones % 5) * 'I'
            elif (ones == 4):
                res += 'IV'
            elif (ones == 5):
                res += 'V'
            elif (ones in [6, 7, 8]):
                res += ('V' + (ones - 5) * 'I')
            elif (ones == 9):
                res += 'IX'

        return res

    def from_roman(roman_num: string) -> int:
        return 0


print(RomanNumerals.to_roman(1990))
# print(RomanNumerals.from_roman('M'))
