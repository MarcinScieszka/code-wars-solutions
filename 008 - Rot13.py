"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be returned as they are. 
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""

def rot13(message):
    ciphered_message = ''
    for character in message:
        t = ord(character) # ASCI representation of chars

        # uppercase letters: A=65, ..., Z=90
        if 65 <= t <= 77:
            ciphered_message += chr(t+13)
        elif 78 <= t <= 90:
            ciphered_message += chr(((t+13) % 91) + 65)
        # lowercase letters a=97, ..., z=122
        elif 97 <= t <= 109:
            ciphered_message += chr(t+13)
        elif 110 <= t <= 122:
            ciphered_message += chr(((t+13) % 123) + 97)
        # other characters returned as they are
        else:
            ciphered_message += character

    return ciphered_message
