"""
Given an integer num, repeatedly add all its digits until the result has only one digit, 
and return it.


Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.


Example 2:
Input: num = 0
Output: 0
"""


def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    num_str = str(num)
    arr = []
    tracker = 0
    for i in range(len(num_str)):
        arr.append(int(num_str[i]))
    for i in range(len(arr)):
        tracker += arr[i]
    while tracker >= 10:
        arr = []
        tracker_str = str(tracker)
        tracker = 0
        for i in range(len(tracker_str)):
            arr.append(int(tracker_str[i]))
        for i in range(len(arr)):
            tracker += arr[i]
    return tracker


t1 = 38
t2 = 0


print(addDigits(t1))
print(addDigits(t2))
