'''
Given an array of integers nums containing n + 1 integers where each integer
is in the range [1, n] inclsuive. 

There is only one repeated number in nums return the this repeated number.

You must solve the problem without modifying the array nums and uses only
constant extra space

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
'''

def findDuplicatesBruteForce(nums):
    dict = {}
    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = 1
        else:
            dict[nums[i]] += 1
    for key in dict.keys():
        if dict[key] > 1:
            return key


def findDuplicateOptimal(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    