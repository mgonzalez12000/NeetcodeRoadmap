"""
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32 bit integer.

You must write an algorithm that runs in O(n) time and without using the division operator

Example 1: Input: nums = [1, 2, 3, 4]
           Output: [23, 12, 8, 6]
Example 2: Input: nums = [-1, 1, 0, -3, 3]
           Output: [0, 0, 9, 0, 0]
"""
# https://leetcode.com/problems/product-of-array-except-self/


def brute(nums):
    result = []
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i != j:
                prod *= nums[j]
        result.append(prod)
    return result


nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]
print("Brute force solution")
print(brute(nums1))
print(brute(nums2))


# Optimal solution
def productExceptSelf(nums):
    leftArr = [1] * len(nums)
    rightArr = [1] * len(nums)
    result = []
    for i in range(1, len(nums)):
        left = nums[i - 1]
        leftArr[i] = left * leftArr[i - 1]
    for i in range(len(nums) - 2, -1, -1):
        right = nums[i + 1]
        rightArr[i] = right * rightArr[i + 1]
    for i in range(len(nums)):
        result.append(leftArr[i] * rightArr[i])
    return result


print("Optimal solution with o(n) time complexity")
print(productExceptSelf(nums1))
print(productExceptSelf(nums2))

"""
Code explanation:
When trying to solve a problem with the most optimal solution it's good if you can come up
with a brute force solution as it can help you come up with an optimal solution as you solve
a brute force solution.

Brute force solution: Use a nested for loop to I allow the algorithm understand when to skip
the current element the loop is iterating through. The first loop's main job is to iterate
through our input array while keep tracking of what index we are on. The second loop
will once again iterate through our array, however, will check if the current index in
which we are iterating through matches the other index in our first loop. If it does, it
means we skip such index and do no include it in our product. Append to our result list with
the product on every loop. Once the loop(s) are done iterating, return our result list.

Optimal solution: These type of solutions require for you to know the "tricks" to come up
with the solution. You either know the trick or don't. For this problem the trick is the
following:
Assume we have the following input array:
[1, 2, 3, 4, 5]
and we are on the 2 index aka element 3... what if we split such array into two, and have
it become a left and right array? We will then have two arrays such that upon full iteration:
left = [1, 1, 2, 6, 24]
right = [120, 60, 20, 5, 1]
result = [120, 60, 40, 30, 24]
if you notice, if we multiply left[i] * right[i] it will equal our result[i].

In code: We will need to initialize two arrays left and right that will first be populated by 1's.
Then we will also initialize an empty result array in which we will append our left[i] * right[i]
at every iteration. First, we will need to populate our left array. We do this by looping through our
input nums starting from the ONE index because we are always looking for the LEFT element. Have a variable
that keeps track of such left element by storing nums[i -1] and then appending to our array such as
leftArr[i] = left * leftArr[i - 1]
Do the same idea for the right array but instead we will be looping backward from the second to last 
element of the array. This time we will be check for the right element by storing nums[i + 1] into a 
right variable and then adding to our rightArr such as rightArr[i] = right * rightArr[i] = right * rightArr[i + 1]
Once these steps are taken we will have two populate leftArr and rightArr arrays. We then just have
to iterate through nums once more time and upon each iteration multiply leftArr[i] * and rightArr[i] and
append our prod to our result array. Return result array
"""
