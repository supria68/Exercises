#Compare two strings by comparing the sum of their values (ASCII character code).

######For comparing treat all letters as UpperCase
######null/NULL/Nil/None should be treated as empty strings
######If the string contains other characters than letters, treat the whole string as it would be empty

#Your method should return true, if the strings are equal and false if they are not equal.

s1 = input("Enter String1:")
s2 = input("Enter String2:")

def charSum(string):
    total = 0
    if(string is None):
        total += ord(' ')
    elif(string.isalpha()):
        for char in string.upper():
            total += ord(char)
    else:
        total += ord(' ')
    return total

if(charSum(s1) == charSum(s2)):
    print('true')
else:
    print('false')


