"""
Given a sorted array of distinct integers
and a target value, return the index if
the target is found. If not, return the
index where it would be if it were
insert in order.

You must write an algorithm with O(log N) runtime
complexity.


Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2


Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1


Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""


def searchInsertBrute(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        else:
            nums.append(target)
            nums = sorted(nums)
            for i in range(len(nums)):
                if nums[i] == target:
                    return i


t1, t1_ = [1, 3, 5, 6], 5
t2, t2_ = [1, 3, 5, 6], 2
t3, t3_ = [1, 3, 5, 6], 7


print(searchInsertBrute(t1, t1_))
print(searchInsertBrute(t2, t2_))
print(searchInsertBrute(t3, t3_))
