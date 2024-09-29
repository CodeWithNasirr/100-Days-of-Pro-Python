# .Print all factors of a given number provided by the user.
user=int(input('enter a number'))
fac=[]
for i in range(1,user+1):
    if (user%i==0) :
        fac.append(i)
print(fac)