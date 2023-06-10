"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in o(n)

Example 1: input: nums = [100, 4, 200, 1, 3, 2]
           output: 4
Example 2: input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
           output: 9

           in progress............
"""


# def longestConsecutive(nums):
#     nums = sorted(nums)
#     left = 0
#     right = len(nums) - 1
#     result = []
#     for i in range(len(nums)):
#         if nums[i] + 1 == nums[i + 1]:
#             result.append(nums[i])
#             result.append(nums[i + 1])
#     return result


# def longestConsecutive(nums):
#     hm = {}
#     result = []
#     nums = sorted(nums)
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         if nums[left] + 1 == nums[left + 1]:
#             result.append(nums[left])
#             result.append(nums[left + 1])
#         elif nums[left] + 1 == None:
#             break
#         left += 1
#     return result


# [100, 4, 200, 1, 3, 2]
# [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
print("original nums")
print(nums)
print()
# sorting list
nums = sorted(nums)
print("sorted nums")
print(nums)
print()
# add to dict
dict = {}
for i in range(len(nums)):
    if nums[i] not in dict:
        dict[nums[i]] = 1
    else:
        dict[nums[i]] += 1
print("dictionary")
print(dict)
print()
tracker = []
for key, value in dict.items():
    if (key in dict and key + 1 in dict) or (key in dict and key - 1 in dict):
        tracker.append(key)
print("tracker")
print(tracker)
print(len(tracker))
