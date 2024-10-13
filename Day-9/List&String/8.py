# Find the frequency of characters in a string.
from collections import Counter
def char_frequency(text):
    return Counter(text)


text="Nasir"
x=char_frequency(text)
print(x)