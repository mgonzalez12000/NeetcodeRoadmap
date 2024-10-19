"""
Given an integer array nums, return true if any value appears more thjan once in the array, otherwise
return false

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
"""
# Test cases
nums = [1, 2, 3, 3]
nums2 = [1, 2, 3, 4]

# Takes in one param of an array of ints, returns a boolean
def hasDuplicateHMApproach(nums):
    # hashmap to take into consideration of occurences. Key will be the int, while the value will keep track of occurences
    # Instatiating a hashmap/dict data structure
    hm = {}
    # Iterate through the elements of ints in nums
    for element in nums:
        # Upon every iteration, if the current element is not in the hm, add it to the hm with a default tracker value of 1
        if element not in hm:
            hm[element] = 1
        # If it is in the hashmap, increase the tracker by one
        else:
            hm[element] += 1
    # Iterate through the hmm, find an instance where the tracker value is greater than 1. If so, there is a duplicate (return true), else no duplicate (return false)
    for key, value in hm.items():
        if value > 1:
            return True
    return False
# print(hasDuplicateHMApproach(nums))


# Hashset approach
def hasDuplicatesHashSetApproach(nums):
    # Instantiate a hashset. Using a hashset because an hs doesnt handle duplciates
    hs = set()
    # Iterate through the input array
    for element in nums:
        # Upon each iteration, if the element doesn't exist in the hs, add the element to the hs
        if element not in hs:
            hs.add(element)
    # Compare lens of both data structures, if len of input array and len of hs are the same, there is no duplicate (return false)
    if len(nums) == len(hs):
        return False
    # Else, if both lenghts are not the same, that means there was a duplicate. (HM does not take into account for duplcaite); return True
    else:
        return True
# print(hasDuplicatesHashSetApproach(nums2))
