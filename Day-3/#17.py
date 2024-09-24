# Write a program that will take three digits from the user and add the square of each digit.

num=int(input("Enter Your Number: "))
a=num % 10
num= num // 10
b=num%10
c=num//10

add=(a**2 + b**2 + c**2)
print(f"Required Number is : {add}")