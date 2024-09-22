# Write a program that will tell whether the given number is divisible by 3 & 6.

user=int(input("Enter a Number: "))

if user%3==0:
    print(f"The {user} is divivsible by 3")
elif user%4==0:
    print(f"The {user} is divivsible by 4")

else:
    print(f"The {user} is Not divivsible by 3 & 6")
