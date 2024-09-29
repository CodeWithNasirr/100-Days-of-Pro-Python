# Write a program to find the euclidean distance between two coordinates.

# Steps of the Euclidean Algorithm:
# 1=>Take two numbers: Let's call them a and b, where a is greater than or equal to b.

# 2=> Divide a by b:
# Compute the remainder when a is divided by b. Let's call this remainder r.

# 3=>Replace a with b and b with r:
# Now, repeat the process by replacing a with b and b with the remainder r.

# 4=>Repeat until the remainder is 0:
# When the remainder becomes 0, the current value of b is the HCF.

x1,y1=1,2
x2,y2=4,6

x=((x1 - x2)**2 + (y1-y2)**2)**0.5
print(x)
