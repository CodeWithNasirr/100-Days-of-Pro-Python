# .User will provide 2 numbers you have to find the by LCM of those 2 numbers


def Lcm(user1,user2):
    a=user1
    b=user2
    while user2 !=0 :
        rem=user1%user2
        user1,user2=user2,rem # yaha per user1 HCF ha and user2 rem 0 ha
    hcf=user1
    lcm=(a*b)//hcf
    print(lcm)
results=Lcm(12,15)
print(f"The LCM of 12 and 15 is: {results}")