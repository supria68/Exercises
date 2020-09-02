#find trailing zeros in the factorial of a given number

# We know that only product of 5 and 2 causes 0 in n!
#since count of 2 > count of 5 -> find only the count of 5 in n!

n = input("Enter the number:")

def trailing_zero(n):
    count = 0
    i = 5
    while(n/i >= 1):
        count += n//i
        i = i * 5 #for 25, 125,....
    return(count)

print(trailing_zero(n))
