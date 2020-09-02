#Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

#persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

num = input("Enter positive number:")
count = 0

if(int(num) < 0):
    print("ERROR!! Enter positive number only")
    quit()
def persistance(numbr):
    if (len(str(numbr)) == 1):
        return 0
    while (len(str(numbr)) > 1):
        global count
        count += 1
        mul = 1
        for i in str(numbr):
            mul = mul * int(i)
        numbr = mul
    return count 

counter_val = persistance(num)
print ("Count value:",counter_val)    
