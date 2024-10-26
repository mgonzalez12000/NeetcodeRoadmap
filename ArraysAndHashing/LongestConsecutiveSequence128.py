"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements
sequence

You must writen an algorithm that runs in O(n)

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
# Test cases
nums1 = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]

def longestConsecutive(nums):
    result = 0
    set_of_nums = set(nums)
    for i in range(len(nums)):
        # Check if the sequence is starting
        if nums[i] - 1 not in set_of_nums:
            counter = 0
            while nums[i] + counter in set_of_nums:
                counter += 1
            result = max(result, counter)
    return result

print(longestConsecutive(nums1))