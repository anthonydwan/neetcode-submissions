# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        if not head.next:
            return head
        
        # p->c ->next
        # p <- c ? next
        prev = None 
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            
            # do the shift
            prev = curr
            curr = temp
        
        return prev
        

