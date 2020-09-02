#Let's define a parameter of number n as the least common multiple (LCM) of the sum of its digits and their product. Calculate the parameter of the given number n.

n = input("Enter the number: ")

def parameter(n):
    total = 0 
    prod = 1
    for i in list(n):
        total = total + int(i)
        prod = prod * int(i)
    #to calculate the LCM
    if total > prod:
        greater = total
    else:
        greater = prod
    while(True):
        if((greater % total == 0) and (greater % prod == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

print(parameter(n))
