"""
Given a 1-index array of integers numbers that is already
sorted in non-decreasing order, frind two numbers such that
they add up to a specific target number. Let these two numbers be
numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length

Return the indices of the two numbers, index, and index, added by one as
an integer array [index1, index2] of length 2

The tests are generated such that there is exactly one solution. You may
not use the same element twice.

Your solution must use only constant extra space

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


nums1= [2, 7, 11, 15]
t1 = 9
nums2 = [2, 3, 4]
t2 = 6
nums3 = [-1, 0]
t3 = -1


def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            return [left + 1, right + 1]


print(twoSum(nums1, t1))
print(twoSum(nums2, t2))
print(twoSum(nums3, t3))


"""
Code exaplanation: Since the input array is sorted from small to greatest, we can use a
two pointer approach by checking if numbers from left + right < target. If it is then
the target, and we know that the input array is sorted, we must increase our left pointer
to check if the next loop will equal the target. Likewise, the other way around, if
left + target > target, then that means we have to "lower" our right number and therefore, 
we will decrease the right pointer. Else, if left and right numbers add up to the target,
then we can simply return an array/list with left and right pointers + 1 to return the
position of the elements, NOT INDEX.
"""