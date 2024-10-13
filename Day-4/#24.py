# Write a program to find the sum of first n numbers, where n will be provided by the user. Eg if the user provides n=10 the output should be 55.

sums=0
user=int(input('Enter a Numebr: '))

for i in range(1,user+1):
    sums+=i

print(sums)