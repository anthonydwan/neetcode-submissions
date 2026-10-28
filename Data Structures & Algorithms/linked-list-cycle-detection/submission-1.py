# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False
        

        s, f = head, head.next

        while s and f:
            if s.val == f.val:
                return True
            s = s.next
            if not f.next:
                return False
            f = f.next.next

        
        return False