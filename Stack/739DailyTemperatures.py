"""
Given an array of integers temperatures represents the daily temperatures, return an array, 
answer such that answer[i] is the number of days you have to wait after the ith day to get
a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead
Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""
# https://leetcode.com/problems/daily-temperatures/solutions/2923400/python-accepted/


def dailyTemperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    stack = []
    answer = [0] * len(temperatures)
    for i in range(len(temperatures)):
        while len(stack) != 0 and temperatures[stack[-1]] < temperatures[i]:
            curr = stack.pop()
            answer[curr] = i - curr
        stack.append(i)
    return answer


input1 = [73, 74, 75, 71, 69, 72, 76, 73]
input2 = [30, 40, 50, 60]
input3 = [30, 60, 90]
print(dailyTemperatures(input1))
print(dailyTemperatures(input2))
print(dailyTemperatures(input3))

"""
Code explanation: to be written
"""
