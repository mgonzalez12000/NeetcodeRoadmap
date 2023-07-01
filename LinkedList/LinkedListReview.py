'''
This script contains fundamental python syntax when working with linkedlist and also contains
fundamental problems that you should be able to easily solve to test your basic knowledge with
linklists.
'''

'''
When working with a linked list, most of the time you will need to make sure that your pointer, or node in this case,
does not go out of bounds. Meaning that the next node is not null. This can be done via a while loop that ensure this
condition. Eg:
while curr.next != null or in a pythonic way while curr.next
'''

'''
Rule of thumb: it is best to store your head node to a variable. You can use such variable to do the following:
Assume you stored the head node in a variable named "current"; current = head
The following methods can be called:
current.next ----> retrieves the next node in the "chain" of the linkedlist.
current.val ----> will retrieve the data/value of the current node that you are on in the LinkedList's chain.
current.next.val -----> will retrieve the data/value of the next node in the chain of the linked list.
In order to continue traversing through the chain, you must do the following within a loop:
current = current.next
'''

'''
What is the different between arrays and a linkedlist? The key differences are the time complexities of each.
Inserting and deleting elements in a list has time complexity O(1). On the otherhand, looking up an element
is expensive because it's time complexity is O(n) as in a linkedlist you must traverse through the entire chain
to reach the element. 
'''

# Remove duplicates from a linkedlist assuming that the nodes are sorted:
def removeDup(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    current = head
    while current.next != None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


# Reverse a linkedlist
def reverse(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev = None
    while head != None:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev
