'''
Given the head of a linked list, remove the nth node from the end of the
list and return its head

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
'''
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummy = ListNode(next = head)
    left = dummy
    right = head

    for i in range(len(n)):
        right = right.next
    while right != None:
        left = left.next
        right = right.next
    left.next = left.next.next

    return dummy.next