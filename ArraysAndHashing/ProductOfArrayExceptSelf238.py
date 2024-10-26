"""
Given an integer nums, return an array answer such that answer[i] is equal to the product of all the elements
of nums except nums[i]

The product of any prefix or suffix of nums is generated to fit in a 32-bit integer

You must write an algorithm that runs in O(n) time and without using the division operation

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
# Test cases
nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]

def bruteForce(nums):
    result = []
    # Outer loop will simply iterate over the input array nums
    for i in range(len(nums)):
        product = 1
        # Second loop will actually multiply the product of non-equal indices
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        # AFter the inner loop exits, append the product to the result array
        result.append(product)
    return result

def optimalSolution (nums):
    result = []
    multiplier = 1
    left = [1] * len(nums)
    right = [1] * len(nums)
    for i in range(len(nums)):
        left[i] *= multiplier
        multiplier *= nums[i]
    multiplier = 1
    for i in range(len(nums) -1, -1, -1):
        right[i] *= multiplier
        multiplier *= nums[i]
    for i in range(len(left)):
        result.append(left[i] * right[i])
    return result
# print(optimalSolution(nums2))
