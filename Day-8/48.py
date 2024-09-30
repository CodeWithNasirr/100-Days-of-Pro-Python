# .The natural logarithm can be approximated by the following series
# formula= x-1/x + 1/2(x-1/x)^i
# If x is input through the keyboard, write a program to calculate the
# sum of the first seven terms of this series.

def natural_loga(x,num):
    total_sum=(x-1)/x
    for i in range(2,num+1):
        total_sum = total_sum + (1/2*((x-1)/x)**i)
        return total_sum
    

print(natural_loga(2,7))