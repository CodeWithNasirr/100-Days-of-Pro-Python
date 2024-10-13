# Write a program to print the first 25 odd numbers
user=int(input("Enter a Number: "))
odd_number=[]
num=1
while(len(odd_number)<user):
    odd_number.append(num)
    num=num+5
print(odd_number)

#Using Function.....


def odd_Numeber(user):
    odd_number=[]
    num=1
    while(len(odd_number)<user):
        odd_number.append(num)
        num+=2
    return odd_number

