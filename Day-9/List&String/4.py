# Merge two sorted lists into one sorted list without using any sorting functions.


# Example usage
l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5, 6, 7]

merged_list=l1+l2
item=[]
for x in merged_list:
    if x not in item:
        item.append(x)

print(item)