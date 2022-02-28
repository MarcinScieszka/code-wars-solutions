"""
Write a function that, given a string of text (possibly with punctuation and line-breaks), 
returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
    A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
    Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
    Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
    Matches should be case-insensitive, and the words in the result should be lowercased.
    Ties may be broken arbitrarily.
    If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, 
    or an empty array if a text contains no words.

Examples:
    top_3_words("In a village of La Mancha, the name of which I have no desire to call to
    mind, there lived not long since one of those gentlemen that keep a lance
    in the lance-rack, an old buckler, a lean hack, and a greyhound for
    coursing. An olla of rather more beef than mutton, a salad on most
    nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
    on Sundays, made away with three-quarters of his income.")
    # => ["a", "of", "on"]

    top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
    # => ["e", "ddd", "aa"]

    top_3_words("  //wont won't won't")
    # => ["won't", "wont"]
"""

from array import array
import re
import string
import unittest

def top_3_words(text: array) -> array:
    top_words = {}

    # if char is not a leter or apostrophe replace it with space
    allowed_chars = string.ascii_lowercase + string.ascii_uppercase + "'"
    for c in text:
        if c not in allowed_chars:
            text = text.replace(c, " ")
 
    # remove duplicate spaces
    text = re.sub(" +", " ", text)

    # remove spaces from the begining and end of the text
    text = text.strip()
    
    words = text.split(' ')
    
    # fill a dict with words as keys and their occurrences as vals
    for word in words:
        # skip empty strings
        if word == '':
            continue

        # skip words containing only apostrophes
        if (re.match("^'+$", word)):
            continue
        
        # words in the result should be lowercased
        word = word.lower()

        if word not in top_words:
            top_words[word] = 1
        else:
            top_words[word] += 1

    # sort dict in descending order and reduce size to top three occuring words  
    top_three_dict =  dict(reversed(sorted(top_words.items(), key=lambda item: item[1])[-3:]))

    return list(top_three_dict.keys())

class TestTopWords(unittest.TestCase):
    def test_return_top_threee_words_from_long_text(self):
        # given
        text = "In a village of La Mancha, the name of which I have no desire to call to mind,      \
            there lived not long since one of those gentlemen that keep a lance in the lance-rack,  \
            an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more       \
            beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays,      \
            and a pigeon or so extra on Sundays, made away with three-quarters of his income."
        
        # then
        self.assertEqual(top_3_words(text), ["a", "of", "on"])
            
    def test_return_top_threee_words_from_text_with_not_allwed_chars(self):
        # given
        text = "  //wont won't won't"

        # then
        self.assertEqual(top_3_words(text), ["won't", "wont"])
    
    def test_return_top_threee_words_from_text(self):
        # given
        text = "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"

        # then
        self.assertEqual(top_3_words(text), ["e", "ddd", "aa"])
    
if __name__ == '__main__':
    unittest.main()
