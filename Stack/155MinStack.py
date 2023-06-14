"""
Design a stack the support push, pop, top, and retrieving the minimum element
in constant time.

Implement the MinStack class:

- MinStack(): initializes the stack object.
- void push(int val): pushes the element val onto the stack.
- void pop(): removes the element on the top of the stack.
- int top(): gets the top element of the stack
- int getMin() retrieves the minimum element in the stack

You must implement a solution with o(1) time complexity for each function
"""
# https://leetcode.com/problems/min-stack/


class MinStack(object):
    def __init__(self):
        self.q = deque()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.q.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.q[-1]

    def getMin(self):
        """
        :rtype: int
        """
        sorting = sorted(self.q)
        result = sorting[0]
        return result


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
Code explanation: Pretty much design and create your own minStack class that implement all the functions
of a Stack data structure. Explanation for each function defined within the class is shown in the
description above. Self explanatory.
"""
