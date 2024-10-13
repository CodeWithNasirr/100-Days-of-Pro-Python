# Check if two strings are anagrams.

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))  # Output: False
