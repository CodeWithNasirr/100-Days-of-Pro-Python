# Write a program that can multiply 2 numbers provided by the user without using the * operator
user1=int(input("Enter a Number: "))#5
user2=int(input("Enter a Number: "))#4
sum=0
for i in range(user1):
    sum+=user2
    # 0 0+4
    # 1 4+4
    # 2 8+4
    # 3 12+4
    # 4 16+4 = 20 
print(sum)