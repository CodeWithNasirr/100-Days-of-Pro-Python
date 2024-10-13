
# Find the longest substring without repeating characters.
a="abcabbbc"
item=[]
for x in a:
    if x not in item:
        item.append(x)

print(len(item))# Output: 3 ("abc")