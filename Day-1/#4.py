# . Write a program that will give you the sum of 3 digits

num1=int(input("Enter a Number1: "))
num2=int(input("Enter a Number2: "))
num3=int(input("Enter a Number3: "))

a=(num1,num2,num3)
print(sum(a))


# Using Functions..

def sum(num1,num2,num3):
    a=sum(num1,num2,num3)
    print(a)
    return a

num1=int(input("Enter a Number1: "))
num2=int(input("Enter a Number2: "))
num3=int(input("Enter a Number3: "))

sum(num1,num2,num3)