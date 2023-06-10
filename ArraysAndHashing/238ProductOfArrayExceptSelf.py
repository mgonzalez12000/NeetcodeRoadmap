"""
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32 bit integer.

You must write an algorithm that runs in O(n) time and without using the division operator

Example 1: Input: nums = [1, 2, 3, 4]
           Output: [23, 12, 8, 6]
Example 2: Input: nums = [-1, 1, 0, -3, 3]
           Output: [0, 0, 9, 0, 0]
"""
# https://leetcode.com/problems/product-of-array-except-self/


nums = [1, 2, 3, 4]

import math

dict = {}
answer = []
for i in range(len(nums)):
    if nums[i] not in dict:
        dict[nums[i]] = math.prod(nums[:i] + nums[i + 1 :])
    answer.append(dict[nums[i]])
print(answer)

"""
Code explanation: Still a work in progress...
"""
