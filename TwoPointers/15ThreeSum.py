"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j and i != k and j != k, and nums[i] + nums[j] + nums[k] == 0
"""
nums = [-1, 0, 1, 2, -1, -4]

left = 0
right = len(nums) - 1
result = []

while left < right:
    sum = nums[left] + nums[right]
    lookup = 0 - sum
    if lookup not in nums:
        right -= 1
    else:
        result.append([nums[left], nums[right],lookup])
        left += 1
print(result)

# This solution is still being worked on