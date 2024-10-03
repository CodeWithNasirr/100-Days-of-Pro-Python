# Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _ – 30%)(0-1lakh print k)


user=float(input("Enter Your Salary: "))
tax=0
temp_salary=0

if (user>2000000) and (user<3000000):
    tax=(30/100)*user
    temp_salary=user-tax


elif (user>1100000) and (user<2000000):
    tax=(20/100)*user
    temp_salary=user-tax

elif (user>2000000) and (user<3000000):
    tax=(30/100)*user
    temp_salary=user-tax
print(f"After Salary Reduction: {temp_salary}")


HR=(10/100) * temp_salary
DA=(5/100)* temp_salary
PF=(3/100)*temp_salary

inhand_salary=(temp_salary-HR-DA-PF)/12
