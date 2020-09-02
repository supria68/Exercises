#find if the number is a perfect square
#A perfect square never ends in 2, 3, 7 or 8
#a perfect square will always have a digital root of 0, 1, 4 or 7

num = input("enter the number:")

def dig_root(num):
    n = int(num)
    if(len(num) == 1):
        return int(num)
    while (len(str(n)) > 1):
        sum = 0
        for i in str(n):
            sum += int(i)
        n = sum
    return sum
    
def is_square(num):
    if(int(num) < 0):
        return False
    if(num[-1] in ["2","3","7","8"]):
        return False
    if (dig_root(num) in [0,1,4,7]):
        return True
    else:
        return False

x = is_square(num)
print(x)

    

