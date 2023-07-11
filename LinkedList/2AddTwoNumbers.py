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
        # l1_stack = []
        # l2_stack = []
        # l1_str = ''
        # l2_str = ''
        # while l1 != None:
        #     l1_stack.append(str(l1.val))
        #     l1 = l1.next
        # while l2 != None:
        #     l2_stack.append(str(l2.val))
        #     l2 = l2.next
        # l1_stack = l1_stack[::-1]
        # l2_stack = l2_stack[::-1]
        # for i in range(len(l1_stack)):
        #     l1_str += l1_stack[i]
        # for i in range(len(l2_stack)):
        #     l2_str += l2_stack[i]
        # return int(l1_str) + int(l2_str)
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 != None or l2 != None or carry:
            if l1 != None:
                v1 = l1.val
            else:
                v1 = 0
            if l2 != None:
                v2 = l2.val
            else:
                v2 = 0
            
            # Compute new digit
            val = v1 + v2 + carry

            # eg: 15
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            # update pointers
            curr = curr.next
            if l1 != None:
                l1 = l1.next
            else:
                None
            if l2 != None:
                l2 = l2.next
            else:
                None
            
        return dummy.next