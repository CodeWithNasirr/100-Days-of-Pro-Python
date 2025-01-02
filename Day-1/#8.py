# Write a program to find the euclidean distance between two coordinates.

# Steps of the Euclidean Algorithm:
# 1=>Take two numbers: Let's call them a and b, where a is greater than or equal to b. (a>=b)

# 2=> Divide a by b:
# Compute the remainder when a is divided by b. Let's call this remainder r.

# 3=>Replace a with b and b with r:
# Now, repeat the process by replacing a with b and b with the remainder r.

# 4=>Repeat until the remainder is 0:
# When the remainder becomes 0, the current value of b is the HCF.

import math

def euclidean_distance(coord1, coord2):
    x1,y1=coord1
    x2,y2=coord2
    distance= math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance
# Example usage
coord1 = (3, 4)
coord2 = (7, 1)

distance = euclidean_distance(coord1, coord2)
print(f"The Euclidean distance between {coord1} and {coord2} is: {distance:.2f}")

