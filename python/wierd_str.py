#Write a function toWeirdCase that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

#The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

str1 = input("Enter the string:")
if (len(str1) % 2 != 0):
    string = str1 + ' '
else:
    string = str1

def to_weird_case(string):
        new_str = ''
        i = 0
        up_case = str(string).upper()
        lw_case = str(string).lower()
        while (i < len(string)):
            new_str = new_str + up_case[i] + lw_case[i+1]
            i = i + 2
        return(new_str.strip())
    
print(to_weird_case(string))

