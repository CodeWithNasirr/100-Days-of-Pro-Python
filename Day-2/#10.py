# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

user_cost=int(input("Enter Your Cost Price: "))
user_sell=int(input("Enter Your Shell Price: "))

if user_cost>user_sell:
    print("You are in a Loss")
else:
    print("You are in a Profit")