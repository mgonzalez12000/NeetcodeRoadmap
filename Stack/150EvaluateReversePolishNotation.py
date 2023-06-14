"""
You are given an array of strings tokens that represent an arithmetic expression in
Reverse Polish Notation: https://en.wikipedia.org/wiki/Reverse_Polish_notation
Evaluate the expression/ Return an integer that represents the value of the operation

Note that:
- The valid operations are '+', '-', '*', and '/'
- Each operand may be an integer or another expression.
- The division between two integers always truncates towards zero.
- There will not be any division by zero
- The input represents a valid arithmetic expression ina reverse polish notation.
- The answer and all the information calculations can be represented in a 32-bit integer

Example 1:
Input: tokens = ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2;
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

nums = ["4", "13", "5", "/", "+"]
stack = []
for i in range(len(nums)):
    if nums[i] == "+":
        tracker = 0
        for i in range(len(stack) - 2, len(stack)):
            tracker += stack.pop()
        stack.append(tracker)
    elif nums[i] == "-":
        tracker = 0
        for i in range(2):
            tracker -= stack.pop()
        stack.append(tracker)
    elif nums[i] == "*":
        tracker = 1
        for i in range(len(stack) - 2, len(stack)):
            tracker *= stack.pop()
        stack.append(tracker)

    elif nums[i] == "/":
        for i in range(len(stack) - 2, len(stack)):
            tracker = stack.pop() / stack.pop()
        stack.append(tracker)

    else:
        stack.append(int(nums[i]))
print(stack)

# stack = [4, 3]
# result = 0
# for i in range(len(stack)):
#     result += stack.pop()
# print(result)
