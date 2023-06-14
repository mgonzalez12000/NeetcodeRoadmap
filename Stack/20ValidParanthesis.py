"""
Given a string s containing just the characters '(', ')', '{', '}', '[', ']'
determine if the input string is valid

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Example 1: Input: s = "()"
           Output: true
Example 2: Input: s = "()[]{}"
           Output: true
Example 3: Input: s = "(]"
           Output: false
"""
# https://leetcode.com/problems/valid-parentheses/


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    result = ""
    dict = {")": "(", "]": "[", "}": "{"}
    stack = []
    for i in range(len(s)):
        if s[i] in dict:
            if len(stack) != 0 and stack[-1] == dict[s[i]]:
                stack.pop()
            else:
                return False
        else:
            stack.append(s[i])
    if len(stack) == 0:
        return True
    else:
        return False


input1 = "()"
input2 = "()[]{}"
input3 = "(]"
print(isValid(input1))
print(isValid(input2))
print(isValid(input3))


"""
Code explanation: The main goal here is to use a stack and dictionary/hashmap to keep track of our chars.
We will have a dictionary/hashmap where they keys will be the closing and values will be the opening.
Iterate through the chars of the string and check whether the current char is in the dictionary, if it is not,
push it onto the stack. If it is in the stack, then check if the stack is not empty, and if the current element
in the dictionary's value matches with the top element in the stack. If it does, pop the element off the stack,
else return false. Finally, check if the stack is empty, if the stack is empty return true, else if the stack is not
empty return false.
"""
