# Find the reverse of a number provided by the user(any number of digit)

user=int(input('enter a number'))
a=int(str(user)[::-1])
# a=list(map(int,str(user)))
# b=a[::-1]
print(a)