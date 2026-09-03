# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next==None:
            return False
        fast=head
        slow=head
        while fast and fast.next and fast!=slow:
            slow=slow.next
            fast=fast.next.next
            if fast.val==slow.val:
                return True
        return False
        