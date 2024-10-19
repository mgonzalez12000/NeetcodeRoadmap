"""
Given two streing s and t, return true if the two strings are anagrams of each other, otherwise
return false

An anagram is a string that contains the exact same characters as another string, but the order of the
character can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false
"""
# Test cases
s1 = "racecar"
t1 = "carrace"

s2 = "jar"
t2 = "jam"

# Accepts 2 input string, returns a boolean type
def isAnagram(s, t):
    hm1 = {}
    hm2 = {}
    # Iterate through input string 1 and keep track with a hm
    for elementS in s:
        if elementS not in hm1:
            hm1[elementS] = 1
        else:
            hm1[elementS] += 1
    # Iterate through input string 2 and keep track with a hm
    for elementT in t:
        if elementT not in hm2:
            hm2[elementT] = 1
        else:
            hm2[elementT] += 1
    # Compare hashmaps with comparison operator
    return hm1 == hm2

# print(isAnagram(s2, t2))