"""
Given a positive integer num, return the number of positive integers less than or equal to num
whose digits sums are even.

The digit sum of a positive integer is the sum of all its digits.


Example 1:

Input: num = 4
Output: 2
Explanation:
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.   


Example 2:

Input: num = 30
Output: 14
Explanation:
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.
"""


def countEven(num):
    arr = []
    tracker = []
    for i in range(1, num + 1):
        arr.append(i)
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            tracker.append(arr[i])
    return tracker


t1 = 4
t2 = 30


print(countEven(t2))
