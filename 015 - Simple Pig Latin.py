"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples:
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text: str) -> str:
    """
    fuction takes text, returns modified text, where the first letter of each word is moved to the end of it, with added "ay"
    punctuation marks are untouched
    """

    result = ''
    for word in text.split():
        # split text by spaces
        if word.isalnum():
            # all the characters are alphanumerical (a-z) and (0-9)
            result += ' ' + word[1:] + word[0] + 'ay'
        else:
            # other characters are untouched
            result += ' ' + word

    return result.lstrip()


print(pig_it('This is my string') == 'hisTay siay ymay tringsay')
print(pig_it('Quis custodiet ipsos custodes ?') == 'uisQay ustodietcay psosiay ustodescay ?')
