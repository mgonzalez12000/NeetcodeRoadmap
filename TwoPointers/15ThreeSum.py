"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j and i != k and j != k, and nums[i] + nums[j] + nums[k] == 0

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums = sorted(nums)
    result = []
    for i in range(len(nums)):
        if i != 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] < 0:
                left += 1
            elif nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return result


nums = [-1, 0, 1, 2, -1, -4]
nums2 = [0, 1, 1]
nums3 = [0, 0, 0]
print(threeSum(nums))
print(threeSum(nums2))
print(threeSum(nums3))


"""
Code explanation: In order to understand this question, I recommend 
fully understanding TwoSum and TwoSumII, and review pointers with a
strong understanding.

Use a for loop to iterate through the input array, while having a left
pointer and right pointer. Use the similar technique/pattern used in TwoSum
(shifting pointers sum < target, sum > target)

Shift left pointer at the end of each iteration of the for loop and then
check if the new element (after shifting left pointer) is the same as the
previos element. If so, shift the left pointer once again.
"""
