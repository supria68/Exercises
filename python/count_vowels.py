#Write a function count_vowels to count the number of vowels in a given string.
#Return nil or None for non-string inputs.

s = input("Enter the string:")

def count_vowels(s):
    vowel_l = ['a','e','i','o','u']
    if(len(s) == 0 or str(s).isdigit()):
        return None
    count = 0
    for i in s.lower():
        if i in vowel_l:
            count += 1
    return count

print(count_vowels(s))
