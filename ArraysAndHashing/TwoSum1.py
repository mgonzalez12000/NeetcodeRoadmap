"""
Given an array of integers nums and an integer target, return the indices i and j
such that nums[i] + nums[j] == target and i !=j

You may assume that every input has exactly one pair of indices i and j that satisfy
the condition

Return the answer with the smaller index first

Example 1:
nums = [3,4,5,6], target = 7
Output: [0,1]

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]
"""
# Test cases
nums1 = [3,4,5,6]
target1 = 7

nums2 = [4,5,6]
target2 = 10

nums3  = [5,5]
target3 = 10

# Takes in nums, a list of integers, and an int target. Returns a list of integers
def twoSum (nums, target):
    # Hashmap will have key as current element of iteration and the value as its index
    hm = {}
    # Iterate through the input array
    for i in range(len(nums)):
        num_bro = target - nums[i]
        # if num bro is not in the hashmap, add the current element and it's index to the hm
        if num_bro not in hm:
            hm[nums[i]] = i
        # Else, the num bro is in the hashmap, which will be the two sum
        else:
            return [hm[num_bro], i]
        
# print(twoSum(nums3, target3))
