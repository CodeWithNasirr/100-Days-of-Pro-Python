# Write a program that will tell whether the number entered by the user is odd or even.

while True:
    user=input('Enter a Number: ')
    if (user=="x"):
        print('TByy')
        break
    else:
        user=int(user)
        if (user % 2 == 0):
            print(f"You Enterd a Even Number {user}")
        else:
            print(f"You Enterd a ODD Number {user}")
   