# Write a program that can find the factorial of a given number provided by the user

fac=1
user=int(input("Enter a Number: "))
for i in range(1,user+1):
    fac *= i
print(fac)