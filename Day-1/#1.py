# User will input (3ages).Find the oldest one
# Simple Way

user1=int(input('Enter Your Age1: '))
user2=int(input('Enter Your Age2: '))
user3=int(input('Enter Your Age3: '))

if user1 > user2:
    print(f'The Oldest one is {user1}')
elif user2 > user3:
    print(f'The Oldest one is {user2}')
else:
    print(f'The Oldest one is {user3}')

# Using Function

def Age_Detector(user1,user2,user3):
    if user1>user2:
        return f"The Oldest one is {user1}"
    elif user2>user3:
        return f'The Oldest one is {user2}'
    else:
        return f'The Oldest one is {user3}'

user1=int(input('Enter Your Age1: '))
user2=int(input('Enter Your Age2: '))
user3=int(input('Enter Your Age3: '))

print(Age_Detector(user1,user2,user3))