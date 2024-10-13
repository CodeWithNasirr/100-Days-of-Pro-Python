# Find all pairs in a list that sum up to a specific target.


def find_pairs(lst, target):
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i],lst[j]))
    return pairs
my_list = [1, 3, 2, 5,35,25,2,15]
print(find_pairs(my_list, 6))  # Output: [(1, 5), (2, 4)]
