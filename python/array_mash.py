#Mash 2 arrays together so that the returning array has alternating elements of the 2 arrays . Both arrays will always be the same length.

#eg. [1,2,3] + ['a','b','c'] = [1, 'a', 2, 'b', 3, 'c']

str1 = input("Enter first array:")
str2 = input("Enter second array:")

if(len(str1) != len(str2)):
    print("Error!! both arrays must be of same length")
    quit()

l1 = str1.split(',')
l2 = str2.split(',')
l3 = []
while True:
    try:
        l3.append(l1.pop(0))
        l3.append(l2.pop(0))
    except:
        break
print(l3)
