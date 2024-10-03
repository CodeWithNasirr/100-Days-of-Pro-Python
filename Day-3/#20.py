# Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _ – 30%)(0-1lakh print k)

user=float(input("Enter Your Salary: "))
tax = 0
temp_salary = user

if (user >500000) and (user < 1000000):
    tax= (10/100) * user
    temp_salary = user - tax
elif (user > 1100000) and (user<2000000):
    tax=(20/100) * user
    temp_salary = user - tax
elif (user > 2000000) and (user<3000000):
    tax=(30/100) * user
    temp_salary = user - tax
    
    print(f"After Salary Reduction: {temp_salary}")
if temp_salary > 500000:
    HR=10/100 * temp_salary
    DA=5/100 * temp_salary
    PF=3/100 * temp_salary
    inhand_salary=(temp_salary - HR - DA - PF)/12
else:
    inhand_salary=(temp_salary)/12

print(f"in Hand Salary is : {inhand_salary}")

if inhand_salary <= 999:
    print(f"{inhand_salary}")
elif inhand_salary > 1000 and inhand_salary<=99999:
    print(f"{inhand_salary/1000}K")
elif inhand_salary > 100000 and inhand_salary<=999999:
    print(f"{inhand_salary/100000}LPA")
else:
    print(f"{inhand_salary/1000000}CR")
