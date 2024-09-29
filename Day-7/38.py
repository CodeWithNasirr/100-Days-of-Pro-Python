# .Take a number from the user and find the number of digits in it

user=int(input('Enter a Number: '))
a=list(map(int,str(user)))
print(len(a))