"""
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.


Example 1:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they 
do not satisfy one or more conditions.  

Example 2:
Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].
"""


def rearrangeArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # one of the main goals is to somehow seperate positive and negatives
    result = []
    positive = []
    negative = []
    # find positives
    for i in range(len(nums)):
        if nums[i] > 0:
            positive.append(nums[i])
    # find negatives
    for i in range(len(nums)):
        if nums[i] < 0:
            negative.append(nums[i])
    # two pointers to add to result lst
    p_pointer = 0
    n_pointer = 0
    while p_pointer <= len(positive) - 1 and n_pointer <= len(negative) - 1:
        result.append(positive[p_pointer])
        result.append(negative[n_pointer])
        p_pointer += 1
        n_pointer += 1
    return result


input1 = [3, 1, -2, -5, 2, -4]
input2 = [-1, 1]
print(rearrangeArray(input1))
print(rearrangeArray(input2))
