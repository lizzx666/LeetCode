'''

Given the head of a singly linked list, reverse the list, and return the reversed list. 

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
            
        return pre




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#recursion
class Solution:
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(curr,pre):
            if not curr:
                return pre
            temp = curr.next
            curr.next = pre
            return reverse(temp,curr)
        return reverse(head,None)



#double pointer
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev_node = None
        while head:
            curr_node = head
            head = head.next
            curr_node.next = prev_node
            prev_node = curr_node
        return prev_node
    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        return prev
