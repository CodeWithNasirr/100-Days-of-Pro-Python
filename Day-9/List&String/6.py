# Remove all occurrences of a specific element from a list.
def remove_element(list,element):
    item=[]
    for x in list:
        if x !=element:
            item.append(x)
    return item
    # return [x for x in list if x!=element]

my_list = [1, 2, 3, 2, 4, 2, 5]
print(remove_element(my_list, 2))  # Output: [1, 3, 4, 5]