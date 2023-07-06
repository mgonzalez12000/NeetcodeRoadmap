'''
Given head, the head of a linked list, determine if the linked list has a cycle
in it.

There is a cycle in a linked list if there is some node in the list that can
be rached again by continously following the enxt pointer. Internally,
pos is used to denote the index of the node and tails next pointer is connected
to. Note that pos is not passed as a parameter. Return true if there is a cycle
in the linked list. Otherwise, return false.
'''
# https://leetcode.com/problems/linked-list-cycle/


# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    slow = head
    fast = head
    while fast != None and fast.next != None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False


'''
Code explanation: Have two pointers, a slow and fast pointer. Where the slow pointer
will iterate one at a time while the fast pointer will move 2 times during every
iteration. If at any point both pointers meet, it means there was a cycle, else there
was no cycle
'''