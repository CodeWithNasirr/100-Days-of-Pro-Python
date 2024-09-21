# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

num=int(input("Enter a Four Digits Number: "))

# r=int(str(num[::-1]))

r=int(str(num)[::-1])
print(f"The Reversed Number is : {r}")
if (num == r):
    print("The reverse is true. The number is a palindrome.")
else:
    print("The reverse is false. The number is not a palindrome.")