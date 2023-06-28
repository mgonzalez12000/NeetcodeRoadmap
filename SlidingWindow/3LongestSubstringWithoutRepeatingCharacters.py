"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
# https://leetcode.com/problems/longest-substring-without-repeating-characters/


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    left = 0
    checker = set()
    maxchecker = 0
    for i in range(len(s)):
        while s[i] in checker:
            checker.remove(s[left])
            left += 1
        checker.add(s[i])
        maxchecker = max(maxchecker, i - left + 1)
    return maxchecker

s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"

print(lengthOfLongestSubstring(s1))
print(lengthOfLongestSubstring(s2))
print(lengthOfLongestSubstring(s3))


"""
Code explanation: 
"""