# Write a program to print all the unique combinations of 1,2,3 and 4
# 2x1=2
# 2x2=4
for i in range(1,5):
    for j in range(1,5):
        if j!= i:
            print(i,j)
        