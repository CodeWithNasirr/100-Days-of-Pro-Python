# Write a program to calculate the sum of the following series till the nth term
# 1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!


def factorial(fac):
    if fac == 0 or fac == 1:
        return 1
    else:
        return fac * factorial(fac-1)
    
def sum_of_series(n):
    total_sum = 0
    for i in range(1,n+1):
        total_sum = total_sum + i / factorial(i)
    return total_sum

n=3
result=sum_of_series(n)
print(f"The sum of the series up to {n} terms is: {result}")
        
