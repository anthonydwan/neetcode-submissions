# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # this is going to be new end
        prev = None
        curr = head

        while curr:
            # save this first
            temp = curr.next
            # fold the direction
            curr.next = prev
            # move to the next set
            prev = curr
            curr = temp

        
        return prev




