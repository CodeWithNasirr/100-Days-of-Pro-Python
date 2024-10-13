# Find the second largest element in a list.
# https://chatgpt.com/share/6701f4bc-1b94-8012-87e7-a7da14420bc6
def find_second_largest(lst):
    # if len(lst)<2:
    #     None
    # f_larget=lst[0]
    # s_larget=lst[0]
    # for x in lst:
    #     if f_larget is None or x>f_larget:
    #         s_larget=f_larget
    #         f_larget=x
    #     elif x!=f_larget and (s_larget is None or x>s_larget):
    #         s_larget=x
    # return s_larget
    x = list(set(lst))
    return x[-2] 
lists = [1,2,3,4,56,12,2,51]
a=find_second_largest(lists)
print(f"Secound Largest Number is : {a}")