# Write a program to find the compound interest
# Formula=>  A = P * (1 + r/n)^(n*t)
def compound_interest(principal, rate, time, n):
    amout=principal*(1+rate%n)**(n*time)
    print(F"AMOUT {amout}")
    intrest=amout-principal
    return round(intrest,2)

# Input from user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time in years: "))
n = int(input("Enter the number of times the interest is compounded per year: "))


x=compound_interest(principal,rate,time,n)
print(x)
