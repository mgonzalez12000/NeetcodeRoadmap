"""
You are given an m x n integer matrix 'matrix' with the following
two properties:
- Each row is sorted in non decreasing order.
- The first integer of each row is greater than the last integer
of the previous row.

Given an integer target, return true if target is in matric or false
otherwise.

You must write a solution in O9log(m *n)) time complexity
"""
# https://leetcode.com/problems/search-a-2d-matrix/


def bruteForce(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return True
    return False


def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    for i in range(len(matrix)):
        left = 0
        right = len(matrix[i]) - 1
        while left <= right:
            middle = (left + right) // 2
            if matrix[i][middle] < target:
                left = middle + 1
            elif matrix[i][middle] > target:
                right = middle - 1
            else:
                return True
    return False


m1, t1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3
m2, t2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13
print(bruteForce(m1, t1))
print(bruteForce(m2, t2))
print(searchMatrix(m1, t1))
print(searchMatrix(m2, t2))


"""
Code explanation:
"""