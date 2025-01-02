# Find the second largest element in a list.
# https://chatgpt.com/share/6701f4bc-1b94-8012-87e7-a7da14420bc6
def find_second_largest(lst):
    # if len(lst)<2:
    #     return None
    # f_largest=s_largest=None
    # for x in lst:
    #     if f_largest is None or x>f_largest:
    #         s_largest=f_largest#4,12,51
    #         f_largest=x#56,
    #     elif f_largest!=x and (s_largest is None or x>s_largest):
    #         s_largest=x
    #     else:
    #         continue
    # return s_largest
    x=list(set(lst))
    return x[-2]

lists = [1,2,3,4,56,12,2,3,4,5,51]
a=find_second_largest(lists)
print(f"Secound Largest Number is : {a}")