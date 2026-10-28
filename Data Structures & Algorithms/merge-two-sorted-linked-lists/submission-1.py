# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        dummy = ListNode()

        l = list1
        r = list2
        node = dummy
        while l and r:
            if l.val < r.val:
                node.next = l
                l = l.next
            else:
                node.next = r
                r = r.next
            node = node.next
        
        if l:
            node.next = l
        if r:
            node.next = r
        
        return dummy.next
