"""
Given two strings s and t return true if t is an
anagram of s, and false otherwise.

An ANAGRAM is a word or phrase formed by rearranging the
letters of a different word or phrase, typically using
all the original letters exactly one.

Example 1: input: s = 'anagram', t = 'nagaram'
           output: true

Example 2: input: s = "rat", t = "car"
           output: false
"""
# https://leetcode.com/problems/valid-anagram/

# Naive approach
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    dict_s = {}
    dict_t = {}
    for i in range(len(s)):
        if s[i] not in dict_s:
            dict_s[s[i]] = 1
        else:
            dict_s[s[i]] += 1
    for i in range(len(t)):
        if t[i] not in dict_t:
            dict_t[t[i]] = 1
        else:
            dict_t[t[i]] += 1
    if dict_s == dict_t:
        return True
    else:
        return False

s1, t1 = 'anagram', 'nagaram'
s2, t2 = 'rat', 'car'
print(isAnagram(s1, t1))
print(isAnagram(s2, t2))

"""
Code explanation: An ANAGRAM, as described, a word(s) or phrase(s) that
contain the same number of letters/char. Knowing this, we can use a
dictionary/hashmap data structure that will allow us to keep track of our
characters. The key will represent that char, while the value will represent
the count. We are creating two dictionaries to keep track of both input
strings. Once both of our dictionaries are populated, we will compare both
dictionaries. If both dictioanries are equal, then both input strings
are indeed anagram. Therefore, we will return TRUE. Otherwise, if both
dictionaries are not equal, we will return FALSE.
"""