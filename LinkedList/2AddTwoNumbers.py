# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_stack = []
        l2_stack = []
        l1_str = ''
        l2_str = ''
        while l1 != None:
            l1_stack.append(str(l1.val))
            l1 = l1.next
        while l2 != None:
            l2_stack.append(str(l2.val))
            l2 = l2.next
        left_1 = 0
        left_2 = 0
        right_1 = len(l1_stack) - 1
        right_2 = len(l2_stack) - 1
        while left_1 < right_1:
            l1_stack[left_1], l1_stack[right_1] = l1_stack[right_1], l1_stack[left_1]
            left_1 += 1
            right_1 -= 1
        while left_2 < right_2:
            l2_stack[left_2], l2_stack[right_2] = l2_stack[right_2], l2_stack[left_2]
            left_2 += 1
            right_2 -= 1

        for i in range(len(l1_stack)):
            l1_str += l1_stack[i]
        for i in range(len(l2_stack)):
            l2_str += l2_stack[i]
        final_num = int(l1_str) + int(l2_str)

        # This was added from solution online.
        l1 = ListNode(0, None)
        l1.val = final_num % 10
        final_num = final_num / 10
        l2 = l1
        while final_num > 0:
            l1.next = ListNode(0, None)
            l1 = l1.next
            l1.val = final_num % 10
            final_num = final_num / 10
        return l2
