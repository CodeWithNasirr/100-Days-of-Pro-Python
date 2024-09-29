# Print the first 20 numbers of a Fibonacci series

# fibonacci ye wo ha jo sum hoga pahle2 series ka

# Example:
# Let’s say we already have the first 5 numbers of the Fibonacci sequence:[0,1,1,2,3]

# Now we want to calculate the next Fibonacci number:

# Step 1: fib_sequence[i-1] (where i = 5 in this case) refers to the last number, which is 3.

# Step 2: fib_sequence[i-2] refers to the second-to-last number, which is 2.

# Step 3: Adding these two gives: 3+2=5

# So, the next Fibonacci number is 5, and it is added to the sequence, which becomes: 



def fib(num):
    fibonacci=[0,1]
    for i in range(2,num):
        add=fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(add)
    return fibonacci

print(fib(20))