# 8. Write a program that will check whether the number is armstrong number or not

# An Armstrong number (also known as a narcissistic number or pluperfect number) for a given number of digits is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

user=int(input("Enter a Number: "))

x=user
a=x%10 
num=x//10
b=num%10
c=num//10
if (a**3 + b**3 +c**3)==user:
    print(f"{user} is a ArmStrong Number")
else:
    print(f"{user} is not a ArmStrong Number")