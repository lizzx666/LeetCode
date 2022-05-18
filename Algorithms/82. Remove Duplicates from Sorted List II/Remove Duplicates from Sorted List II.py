'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. 
Return the linked list sorted as well.

 

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]


Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

'''


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pre = ListNode(0)
        dummy.next = head
        
        
        while head and head.next:
            if head.next.val == head.val:
                while head and head.next and head.next.val == head.val:
                    head = head.next
                head = head.next
                pre.next = head
            
            else:
                pre = pre.next
                head = head.next
                
        return dummy.next
       
       
 
 
 class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pre = ListNode(0)
        dummy.next = head
        
        cur = head
        
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next
                
            else:
                pre = pre.next
            
            cur = cur.next
            
        return dummy.next
       
       
