"""
A phrase is a palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include
letters and numbers

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""
#https://leetcode.com/problems/valid-palindrome/


# Naive/brute force solution. NOT RECOMMENDED
def brute(s):
    s = ''.join(filter(str.isalnum, s))
    s = s.lower()
    if s == s[::-1]:
        return True
    return False

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = ''.join(filter(str.isalnum, s))
    s = s.lower()
    left = 0
    right = len(s) - 1
    
    while left < len(s) and right >= 0:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


s1 = 'A man, a plan, a canal: Panama'
s2 = 'race a car'
print('brute force solution:')
print(brute(s1))
print(brute(s2))
print('Optimal solution using pointers:')
print(isPalindrome(s1))
print(isPalindrome(s2))

"""
Code explanation:
Naive/brute force approach: The naive approach for this problem is to use
Python's powerful string slicing technique. Although this solution is correct,
interviewrs are not looking for this. Or will follow up and ask you if you
can solve the problem without any built-in Python features. This is where
POINTERS come into play!!!

Optimal approach: Create two pointer, where one will iterate from left to right
and the other will iterate from right to left. Both pointers will iterate
through the entire iterable (input string). Using a while loop, we can insure
that our pointers do not go out of range, and during every iteration, we can check
if the chars from both the left side and right side equal one another, we increase
our left pointer while also decreasing our right pointer. If it any point the left
character and right character DO NOT match, that means the string is not a palindrome.
At that point, we break out of the loop by somply returning false. However, if
the loop finishes ececuting per the conditions given above, then we return True.

Note: For both solutions, in order to get rid of non-alphaNumericals/spaces chars in the string
we are using Python ''.join() and filtering out non=alphaNumericals by filter(str.islanum,s)
where the second argument MUST be an iterable. In this case, our input string
"""
