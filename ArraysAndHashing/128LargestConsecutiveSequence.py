"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in o(n)

Example 1: input: nums = [100, 4, 200, 1, 3, 2]
           output: 4
Example 2: input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
           output: 9
"""
# https://leetcode.com/problems/longest-consecutive-sequence/


def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    hash_set = set(nums)
    longest = 0
    counter = 0
    for i in range(len(nums)):
        if nums[i] - 1 not in hash_set:
            counter = 1
            while nums[i] + counter in hash_set:
                counter += 1
            longest = max(longest, counter)
    return longest


test1 = [100, 4, 200, 1, 3, 2]
test2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longestConsecutive(test1))
print(longestConsecutive(test2))

"""
Code explanation: A sequence is when the ints are in order with increments by one.
We are going to use a hashset data structure to "back track" and check whether
our current element, upon iteration, is in a sequence. Upon every iteration we
will check if the previous element exists in our hashset. If it does not, it means
we are at the start of a sequence adn therefore set our counter at 1. 
We then use a while loop to back track to our hashset and see if the "next" element 
is in our hashset, if so, we increase our counter. Then we check for the mac tracker.
"""
