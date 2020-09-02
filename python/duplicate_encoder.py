#The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

str1 = input("Enter the string:")

dict_l = {}
for char in list(str1.lower()): #get histogram for the repition
    dict_l[char] = dict_l.get(char,0) + 1

for i,c in dict_l.items(): #if letter is repeated, replace it with ')' else '('
    if(c > 1):
        out_str = str1.lower().replace(i,')')
    else:
        out_str = str1.lower().replace(i,'(')
    str1 = out_str
print(str1)
