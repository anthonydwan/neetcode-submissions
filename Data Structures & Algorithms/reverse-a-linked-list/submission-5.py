# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #  prev --> curr --> next
        #  prev -- 

        if not head:
            return None
        
        if not head.next:
            return head
        
        # before reversing, you still have reference to original next
        node = self.reverseList(head.next)

        # reverse
        head.next.next = head
        head.next = None

        
        return node

