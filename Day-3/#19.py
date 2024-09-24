# Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.

user=int(input("Enter a Number: "))

x=user

a=x%10
num=x//10
b=num%10
num=num//10
c=num%10
d=num//10
if (a**4 + b**4 + c**4 + d**4) ==user:#9474
    print("It is a narcissist numebr ")
else:
    print("It is not a narcissist numebr ")