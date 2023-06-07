"""
Given an integer array nums and an integer k, return the k
most frequent elements. You may return the answer in any order

Example 1: input: nums = [1, 1, 1, 2, 2, 3], k = 2
           output: [1, 2]
Example 2: input: nums = [1], k = 1
           output: [1]
"""
# https://leetcode.com/problems/top-k-frequent-elements/

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    hashmap = {}
    result = []
    for i in range(len(nums)):
        if nums[i] not in hashmap:
            hashmap[nums[i]] = 1
        else:
            hashmap[nums[i]] += 1
    sorted_hm = sorted(hashmap, key = hashmap.get, reverse = True)
    for i in range(k):
        result.append(sorted_hm[i])
    return result

test1nums = [1, 1, 1, 2, 2, 3]
test1k = 2
print(topKFrequent(test1nums, test1k))

"""
Code explanation: We are going to use a hashmap to keep track of our occurences
for each element in our input array where the keys will be the elements
and the values will be the count. We begin by iterating through the input
array and check if such element already exists in the hashmap. If it does not,
append to it. If it is already in the hashmap increase its value by 1. Once we
have our hashmap populated, we will need to sort our hashmap's key in reverse
based on the values (count occurences). Doing so, we are now able to create a
loop that will iterate k times through our newly sorted list to grab the top k
elements. We can append these elements into an empty list and return such populated
list
"""