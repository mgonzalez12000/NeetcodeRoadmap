"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.


Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""


# This solution is WRONG, still working on it
def isIsmorphic(s, t):
    hm = {}
    res_lst = []
    for x, y in zip(s, t):
        hm[x] = y
    if len(s) != len(t):
        return False
    for x, y in zip(s, t):
        res_lst.append(hm[x] == y)
    if False in res_lst:
        return False
    return True


print(isIsmorphic("egg", "add"))
