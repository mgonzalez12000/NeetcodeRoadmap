"""
Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums, if target
exists, then return its index. Otherwise, return -1

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""
# https://leetcode.com/problems/binary-search/


def search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] < target:
            left = middle + 1
        elif nums[middle] > target:
            right = middle - 1
        else:
            return middle
    return - 1
        

nums1, t1 = [-1, 0, 3, 5, 9, 12], 9
nums2, t2 =  [-1,0,3,5,9,12], 2
print(search(nums1, t1))
print(search(nums2, t2))
# Consider understanding overflow with middle = left + ((right - left) // 2)


"""
Code explanation: Just like the real worl example given in this chapters review,
think of a file cabinet tring to find files (portfolio). You middle pointer is
your target. Shift left and right pointers accordingly.
"""