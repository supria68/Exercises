"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""

def anagrams(word, words):
    word_ascii = 0
    return_list = []

    for char in list(word):
        word_ascii += ord(char) # word - ascii count

    for each in words:
        each_ascii = 0
        for char in list(each):
           each_ascii  += ord(char)
        if each_ascii == word_ascii:
            return_list.append(each)

    return return_list

array = anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
print(array)



