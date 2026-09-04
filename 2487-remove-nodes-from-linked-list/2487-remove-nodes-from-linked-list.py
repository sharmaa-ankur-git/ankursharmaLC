# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)
        dummy = ListNode(0)
        curr = dummy
        max_so_far = float('-inf')
        while head:
            if head.val >= max_so_far:
                max_so_far = head.val
                curr.next = head
                curr = curr.next
            head = head.next  
        curr.next = None 
        return self.reverse(dummy.next)

        