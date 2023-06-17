"""
You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of ht eith line are (i, 0) and
(i, height[i]).

Find two lines that together with the x-axis form a container, such that
the continar contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""


def maxArea(height):
    left = 0
    right = len(height) - 1
    math = 0
    result = 0
    while left < right:
        math = min(height[left], height[right]) * (right - left)
        result = max(result, math)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return result

input1 = [1,8,6,2,5,4,8,3,7]
input2 = [1,1]
print(maxArea(input1))
print(maxArea(input2))


"""
Code explanation: We are going to use a two pointer approach to check
whether our left or right pointer is smaller than the other is so we
will increase/decrease according. Upon every iteration and before
increasing/decreasing pointers, we will get the amaount of water
between each pillar aka area.
This is done by the following math equation: small pillar * width between
both pillars.
The reason we are using the smaller pillar for the height is because
if we were to use the bigger pillar, where a smaller pillar already exists,
water will overflow. Therefore, we must always take the smaller pill
into consideration.
Finally return the result.
"""