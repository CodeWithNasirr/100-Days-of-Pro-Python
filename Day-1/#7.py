# Write a program that will tell whether the given year is a leap year or not.


user=int(input("Enter a Year: "))

if (user%4)==0:
    if (user%100==0):
        if (user%400==0):
            print(f"{user} is a Leaf Year ")
        else:
            print(f"{user} is Not a Leaf Year ")
    else:
        print(f"{user} is a Leaf Year ")
else:
    print(f"{user} is not a Leaf Year ")
