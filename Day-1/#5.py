# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

num=int(input("Enter a Four Digits Number: "))

# r=int(str(num[::-1]))

r=int(str(num)[::-1])#just imagine you have list a=[1234] you have to convert this into [4321] if u use this print(a)[::-1] it not work bcz the number is in int so sliceing also convert the string so you have to do firstly to convert the integer into strings then it work  
print(type(r))

print(f"The Reversed Number is : {r}")
if (num == r):
    print("The reverse is true. The number is a palindrome.")
else:
    print("The reverse is false. The number is not a palindrome.")
