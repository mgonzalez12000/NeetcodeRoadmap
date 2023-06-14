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

nums = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]


def evalRPN(nums):
    stack = []
    temp = []
    count = 0
    for i in range(len(nums)):
        if nums[i] == "+":
            temp.append(stack.pop())
            temp.append(stack.pop())
            count = temp.pop() + temp.pop()
            stack.append(count)
            print('after adding into stack', stack)
        elif nums[i] == "-":
            temp.append(stack.pop())
            temp.append(stack.pop())
            count = temp.pop() - temp.pop()
            stack.append(count)
            print('after subtracting from stack', stack)
        elif nums[i] == "*":
            temp.append(stack.pop())
            temp.append(stack.pop())
            count = temp.pop() * temp.pop()
            stack.append(count)
            print('after multiplying from stack', stack)
        elif nums[i] == "/":
            temp.append(stack.pop())
            temp.append(stack.pop())
            count = temp.pop() / temp.pop()
            count = int(count)
            stack.append(count)
            print('after dividing from stack', stack)
        else:
            stack.append(int(nums[i]))
            print('after inserting into stack', stack)
    return count

print(evalRPN(nums))


