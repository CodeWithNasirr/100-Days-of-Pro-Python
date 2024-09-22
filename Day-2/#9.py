# Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.

a=int(input('Enter Your 1st Number: '))
b=int(input('Enter Your 2st Number: '))
c=int(input('Enter Your 3st Number: '))

if (a + b + c == 180) and a!=0 and b!=0 and c!=0:
    print("Possible")
else:
    print("Not Possible")
