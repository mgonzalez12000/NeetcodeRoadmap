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


def evalRPN(nums):
    """
    :type tokens: List[str]
    :rtype: int
    """

    stack = []
    temp = []
    count = 0
    for i in range(len(nums)):
        if nums[i] == "+":
            temp.append(stack.pop())
            temp.append(stack.pop())
            count = temp.pop() + temp.pop()
            stack.append(count)
        elif nums[i] == "-":
            temp.append(stack.pop())
            temp.append(stack.pop())
            count = temp.pop() - temp.pop()
            stack.append(count)
        elif nums[i] == "*":
            temp.append(stack.pop())
            temp.append(stack.pop())
            count = temp.pop() * temp.pop()
            stack.append(count)
        elif nums[i] == "/":
            temp.append(stack.pop())
            temp.append(stack.pop())
            count = temp.pop() / temp.pop()
            count = int(count)
            stack.append(count)
        else:
            stack.append(int(nums[i]))
    return count


test1 = ["2", "1", "+", "3", "*"]
test2 = ["4", "13", "5", "/", "+"]
test3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalRPN(test1))
print(evalRPN(test2))
print(evalRPN(test3))

"""
Code explanation: Iterate through our input array and check whether the element is a special character
such as +, -, *, or /. If not, then we add the string, convert to an int by casting, and pushing to our
stack. If at any point we iterate over a special element (noted above), we pop the last two elements
pushed into our stack and add those popped values to a new temp stack. The reason for this is to re organize
the elements to pop/compute the math in the correct order. We then compute the math with the popped values
from our temp stack, and push our answer from the math to our regular stack. Repeat this process until
we finish our iterations through the entire input array.

Trick/Tip: For /, in order to round down when getting decimal answer, convert the answer to an int type by
casting an int to your ans variable. This will round down decimals. Eg: 2.6 will round down to 2.
NOTE: This only works for Python 3
"""
