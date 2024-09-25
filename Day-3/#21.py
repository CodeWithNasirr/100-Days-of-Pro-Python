# Write a menu driven program - 1.cm to ft 2.kl to miles 3.usd to inr 4.exit

user=int(input(''''
            Hello Guys Welcome
        1- Convert Cm to inches
        2- Convert KM to miles
        3- Covert USD to INR
        4- Exit \n
        '''))

if user == 1:
    CM=float(input("Enter Value in Cm: "))
    inchs=user * 0.394
    print(f"Your Value in inches is {inchs}")
elif user ==2:
    KM=float(input("Enter Value in KM: "))
    miles= KM * 0.621
    print(f"Your Value in Miles is {miles}")
elif user ==3 :
    USD=float(input("Enter Value in USD: "))
    INR= USD * 83
    print(f"Your Value in INR is {INR}")
elif user == 4:
    exit() 



