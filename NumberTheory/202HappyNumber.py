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
    str_num = str(n)
    sum = 0
    for i in range(len(str_num)):
        sum += int(str_num[i]) ** 2
    while sum > 1:
        str_sum = str(sum)
        sum = 0
        for i in range(len(str_sum)):
            sum += int(str_sum[i]) ** 2
        print(sum)


t1 = 19
t2 = 2


print(isHappy(t2))
