# Implement your own version of Python’s split() method.

def custom_spilt(text,space=" "):
    item=[]
    temp=""
    for char in text:
        if char == space:
            item.append(temp)
            temp=""
        else:
            temp+=char
        
    if char:
        item.append(temp)
    
    return item


text="Iam Nasir The sk"
x=custom_spilt(text)
print(x)