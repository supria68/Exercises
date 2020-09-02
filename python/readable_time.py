#Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

#HH = hours, padded to 2 digits, range: 00 - 99
#MM = minutes, padded to 2 digits, range: 00 - 59
#SS = seconds, padded to 2 digits, range: 00 - 59
#The maximum time never exceeds 359999 (99:59:59)

sec = input("Enter seconds:")
if(int(sec) > 359999):
    print("The maximum time never exceeds 359999!!")
    quit()

def mark_readable(sec):
    hour = int(sec) // 3600
    minute = (int(sec) % 3600) // 60
    second = (int(sec) % 3600) % 60
    return("{:02d}:{:02d}:{:02d}".format(hour, minute, second))

mark_readable(sec)


