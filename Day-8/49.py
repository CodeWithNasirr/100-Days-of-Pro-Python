# Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.


# total_sum=0
# i=0
# while True:
#     user=input("Enter a Number: ")
#     if user.lower()=='done':
#         break
#     else:
#         user=float(user)
#         total_sum+=user
#         i+=1

# if i>0:
#     avg=total_sum/i
#     print(f"Sum of Number: {total_sum}")
#     print(f"Avg of Number: {avg}")
# else:
#     print(f"No Number Entred Here...")


# using Functions


# def Cal_Avg():
#     number=[]
#     while True:
#         user=input("Enter a Number: ")
#         if user.lower()=='done':
#             break
#         try:
#             user=float(user)
#             if user:
#                 number.append(user)
#         except ValueError:
#             print('Enter a Valid Number')
#     if number:
#         return sum(number)/len(number)

# print(f"The Avg Vlaue is :{Cal_Avg()}")