"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique

You may return the output in any order

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]
"""

# Test cases:
nums1 = [1,2,2,3,3,3]
k1 = 2
nums2 = [7,7]
k2 = 1

# Takes in an array of integers and returns an array of integers. Returned array can be in any order. The element in the returned array represent the top k frequent elementsr
def topKFrequent(nums, k):
    result = []
    hm = {}
    # Populate hashmap with element as key and occurence tracker as the value
    for element in nums:
        if element not in hm:
            hm[element] = 1
        else:
            hm[element] += 1
    # Sort the hashmap with the top most frequent element to the less most frequent elemenent. TLDR: Greatest to least
    sorted_element_freq = sorted(hm, key=hm.get, reverse=True)
    # Loop until k and append the top k frequent element to result array
    for i in range(k):
        result.append(sorted_element_freq[i])
    return result
# print(topKFrequent(nums1, k1))