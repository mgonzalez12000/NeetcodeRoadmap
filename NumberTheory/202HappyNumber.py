"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the square of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in
a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy

Return true if n is a happy number, and false if not


Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Example 2:

Input: n = 2
Output: false
"""


def isHappy(n):
    while len(str(n)) > 1:
        count = 0
        for x in str(n):
            count += int(x) ** 2
        n = count
    if n != 1 and n != 7:
        return False
    else:
        return True


t1 = 19
t2 = 2


print(isHappy(t1))
print(isHappy(t2))
