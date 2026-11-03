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
        
        # got to reverse the subproblem first
        temp = self.reverseList(head.next)

        # reverse it
        head.next.next = head
        # cut the current's connection
        # reattached in next round if needed
        head.next = None

        return temp