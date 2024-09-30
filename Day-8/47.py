# . Write a Python Program to Find the Sum of the Series till the nth term:
# 1 + x^2/2 + x^3/3 + … x^n/n


def sum_series(x,n):
    total_sum=1
    for i in range(1,n+1):
        total_sum+=(x**i)/i
x=2
n=3

print(f"The sum of the series for x={x} and n={n} is: {sum_series(x, n)}")