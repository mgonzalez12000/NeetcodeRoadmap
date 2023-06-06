"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to
target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order

Example 1: input: nums = [2, 7, 11, 15], target = 9
           output: [0, 1]
Example 2: input: nums = [3, 2, 4], target = 6
           output: [1, 2]
Example 3: input: nums = [3, 3], target = 6
           output: [0, 1]
"""
# https://leetcode.com/problems/two-sum/

# Naive approach
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}
    result = []
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in dict:
            result.append(i)
            result.append(dict[difference])
        if nums[i] not in dict:
            dict[nums[i]] = i
    return result

# Optimal approach
def optimalTwoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}
    result = []
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in dict:
            result.append(i)
            result.append(dict[difference])
        dict[nums[i]] = i
    return result


nums1, target1 = [2, 7, 11, 15], 9
nums2, target2 = [3, 2, 4], 6
nums3, target3 = [3, 3], 6
print('Naive solution')
print(twoSum(nums1, target1))
print(twoSum(nums2, target2))
print(twoSum(nums3, target3))
print('Optimal solution')
print(optimalTwoSum(nums1, target1))
print(optimalTwoSum(nums2, target2))
print(optimalTwoSum(nums3, target3))

"""
Code explanation: The main goal for this problem is to find two elements
indeces that sum to the target input. In order to do so, we will use a
hashmap/dictionary data structure to keep track of our chars and respective
index. Where the key will be the char and the value will be the index.
We will also initiate a list where we will later populate with the correct
indeces.

We begin with iterating through the nums input list of ints. Through
every iteration of the loop, we will do the following three things:
- Since we are guranteed that each element in the input list is unique,
  we will add it to the dictionary/hashmap without checking for duplicates
- We will also check for a "difference". This difference will be checked if
  it exists in another position of our input list. This can be done as
  difference = result - nums[i]
- If the difference is found in the dictionary from previous iterations of
  the loop, then we will add to our result list. We will add the index of
  the current char we are looping through to our result list, and the 
  value (index) of our difference key found.
"""
        