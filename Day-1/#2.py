# Write a program that will convert celsius value to fahrenheit
# user*9/5 + 32 Formula
# Simple WAy
# user=int(input("Enter a No That Will Convert into fahrenheit: "))

# x=user*9/5 + 32
# print(f"{user} Celsius is convert Into {x} Fahreheit")


# Using Functions

def Temp_converter(user):
    x=user*9/5 + 32
    print(f"{user} Celsius is convert Into {x} Fahreheit")
    return x
user=int(input("Enter a No That Will Convert into fahrenheit: "))

Temp_converter(user)

