# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                while slow!=fast:    # (after setting the slow to head and fast being at it's last position when made to 
                    slow=slow.next   #  move on step at time then they would meet at common point which would be the start
                    fast=fast.next   #  of the cycle)
                return slow
        return None


        