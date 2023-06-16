"""
Pointers is a trickey concept to grasp. This script will go over basic
review on how pointers work and how to implement them.

All what pointers are really are INDECES which you are POINTING to in an
iterable like a list/array and string.
"""

# Assume we want to iterate through the entire lst, from left to right
# by using pointers only. That can be done the following way.
# Assume we are given the folloing lst:
lst= [1, 2, 3, 4, 5]
# We need to initialize our pointer at 0 since we need to start at the 0 index
# after every iteration we increase our pointer. We stop the iteration once
# a condition is met. In this case our pointer var value canot be greater than
# the length of the list.
pointer = 0
while pointer < len(lst):
    print(lst[pointer])
    pointer += 1
# This prints 1, 2, 3, 4, 5

# Now what if we want to iterate backwards from an iterable? Same concept applies,
# but now we are going to start our pointer at the last index of our iterable and
# decrease our pointer by 1 after each iteration until the condition is met.
pointer_two = len(lst) - 1
while pointer_two >= 0:
    print(lst[pointer_two])
    pointer_two -= 1
# This will pront 5, 4, 3, 2, 1


