# Write a program to find the simple interest when the value of principle,rate of interest and time period is given.

p=int(input("Enter Your Prinsiple: "))
r=int(input("Enter The Rate Intrest: "))
t=int(input("Enter The Time Period of year: "))

x= (p*r*t)/100
print(f"Your Simple Intrest is: {x}")
print(f"Your Amout is {p}")