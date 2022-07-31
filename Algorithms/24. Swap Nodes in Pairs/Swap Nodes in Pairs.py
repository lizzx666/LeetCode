'''
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        curr = dummy_head
        
        while curr.next and curr.next.next:
            temp1 = curr.next
            temp2 = curr.next.next.next
            
            curr.next = curr.next.next
            curr.next.next = temp1
            temp1.next = temp2
            
            curr = curr.next.next
            
        return dummy_head.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy
        
        while head and head.next:
            first_node = head
            second_node = head.next
        
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
        
            prev_node = first_node
            head = first_node.next
        return dummy.next
