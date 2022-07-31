'''


Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        fast, slow = dummy_head, dummy_head
        while n:
            fast = fast.next
            n-=1
        while fast.next:
            fast = fast.next
            slow = slow.next
        #when fast points to last element, slow points to the element before the element need to be deleted
        slow.next = slow.next.next
        return dummy_head.next
