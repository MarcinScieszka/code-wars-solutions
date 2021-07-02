"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. 
For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false


Write a function that will find all the anagrams of a word from a list. 
You will be given two inputs a word and an array with words. 
You should return an array of all the anagrams or an empty array if there are none. 
For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""

from collections import Counter

def anagrams_0(word, words):
    out = []

    # couting occurences of letters in original word
    counted_letters = dict(Counter(word))

    for curr_word in words:
        # couting occurencces of letters in each word that is compared
        counted_letters_curr_word = dict(Counter(curr_word))

        if counted_letters == counted_letters_curr_word:
            out.append(curr_word)
    
    return out

def anagrams_1(word, words):
    # shorter representation of function above
    counted_letters = Counter(word)

    return [curr_word for curr_word in words if Counter(curr_word) == counted_letters]
