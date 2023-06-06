"""
Given an integer array nums, return true if any value appears at least
twice in the array, and return false if every element is distinct

Example 1: input: nums = [1, 2, 3, 1]
           output: true
Example 2: input: nums = [1, 2, 3, 4]
           output: false
Example 3: input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
           output: true
"""
# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    hashSet = set()
    for i in range(len(nums)):
        if nums[i] not in hashSet:
            hashSet.add(nums[i])
    if len(hashSet) == len(nums):
        return False
    else:
        return True

testOne = [1, 2, 3, 1]
testTwo = [1, 2, 3, 4]
testThree = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(containsDuplicate(testOne))
print(containsDuplicate(testTwo))
print(containsDuplicate(testThree))