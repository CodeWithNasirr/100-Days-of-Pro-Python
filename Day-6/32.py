# .User will provide 2 numbers you have to find the HCF of those 2 Number HCF = Highest Common Factor & GCD (Greatest Common Divisor):

# Steps of the Euclidean Algorithm:
# 1=>Take two numbers: Let's call them a and b, where a is greater than or equal to b.

# 2=> Divide a by b:
# Compute the remainder when a is divided by b. Let's call this remainder r.

# 3=>Replace a with b and b with r:
# Now, repeat the process by replacing a with b and b with the remainder r.

# 4=>Repeat until the remainder is 0:
# When the remainder becomes 0, the current value of b is the HCF.


# Example:
# Let’s find the HCF of 48 and 18 using the Euclidean algorithm.

# Step 1: Start with 48 and 18. Divide 48 by 18.
# 48÷18=2 remainder 12. So Replace a =18 ,b= 12 

# Step 2: Now divide 18 by 12.
# 18÷12=1 remainder 6. So Replace a =12 ,b= 6

# Step 3: Now divide 12 by 6.
# 12/6=2 Reminder is 0 

# When the remainder is 0, the current divisor is 6.
# Thus, the HCF of 48 and 18 is 6.

# Taking input from the user
user1 = int(input("Enter Your First Number: "))
user2 = int(input("Enter Your Second Number: "))

while(user2 != 0):
    reminder=user1%user2
    user1,user2=user2,reminder

print(f"The Results: {user2}")
print(f"The HCF is: {user1}")