"""
Given the head of a singly linked list, reverse the list, and return
the reversewd list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
"""
# https://leetcode.com/problems/reverse-linked-list/description/

def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    previous = None
    while head != None:
        temp = head
        head = head.next
        temp.next = previous
        previous = temp
    return previous


"""
Code explanation: Loop through the linkedlist by making sure that the current
visited node is not null. Initialize a temp variable to store the current value
of the head, iterate forward in the LL chain, change pointer to original node, 
and finally change previous pointer to the original node that we were on as head.
"""