# Find the maximum and minimum elements in a list without using in-built functions.



def max_min(number):
    if len(number)==0:
        None,None
    max=number[0]
    min=number[0]
    for x in number:
        if x > max:
            max = x
        elif x<min:
            min = x
        
    return max,min




list=[1,2,3,5,6,8,92,12,42]

max,min=max_min(list)
print(f"Max Number is {max}")
print(f"Min Number is {min}")