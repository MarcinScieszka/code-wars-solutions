"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case).

Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""

def to_camel_case(text):
    if len(text) == 0:
        return text

    first_letter = text[0]

    # replace every dash with underscore and devide text into words
    text = text.replace('-', '_').split('_')

    converted_text = ''
    for word in text:
        # each word starts with capital letter 
        converted_text += word.capitalize()

    if first_letter != converted_text[0]:
        # first letter from the original text has to be preserved
        converted_text = first_letter + converted_text[1:]

    return converted_text
