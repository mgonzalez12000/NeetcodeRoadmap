"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""
# https://leetcode.com/problems/generate-parentheses/


def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """

    stack = []
    res = []

    def backTrack(open, close):
        if open == close == n:
            res.append("".join(stack))
            return
        if open < n:
            stack.append("(")
            backTrack(open + 1, close)
            stack.pop()
        if close < open:
            stack.append(")")
            backTrack(open, close + 1)
            stack.pop()

    backTrack(0, 0)
    return res


test1 = 3
test2 = 1
print(generateParenthesis(test1))
print(generateParenthesis(test2))


"""
Code explanation: Create a recursive algorithm with a helper function. This helper function will
continue to run until the base case is met. Then the function will STOP aka return.

Keep this rule of thumb:
- If our # of opening parenthesis < n input given; that means we can add an opening parenthesis
- If our # of closing parenthesis < opening parenthesis; that means we can add a closing parenthesis
During each condition you will either append a '(' or ')' accordingly to a stack, and increase open,
close arguments by 1 (+1) accordingly. End both condition by popping from the stack.
Finally call the helper function, and passing values of 0, and return your res

Base Case explained: 
Once the # of opening parenthesis, closing parenthesis, and input n equal each other, it will combing all
elements to a string. Append the result to a res [].
"""
