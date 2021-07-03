"""
Given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example:

alphabet_position("The sunset sets at twelve o' clock.")

Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
"""

# provide 'abcdefghijklmnopqrstuvwxyz'
from string import ascii_lowercase 

def alphabet_position(text):
    # genereate dict where {'a': 1, 'b': 2, ..., 'z': 26}
    repacements = {letter.lower():i+1 for i, letter in enumerate(ascii_lowercase)}

    output_string = ''
    for character in text:
        if character.lower() in repacements:
            # lower() used to account for upper letters
            output_string += ' ' + str(repacements[character.lower()]) 
    
    return output_string.strip() # strip() used to remove unwanted space
