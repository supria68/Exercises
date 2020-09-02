#You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

#Array can contain numbers or strings. X can be either.

#Return true if the array contains the value, false if not.

list_inp = input("Enter the sequence:")
seq = list_inp.split(',')
print(seq)
ele = input("Enter the element to be found:")

def check(seq, ele):
    for i in seq:
        x = str(i).find(ele)
    if (x == -1):
        return False
    else:
        return True

x = check(seq,ele)
print(x)
