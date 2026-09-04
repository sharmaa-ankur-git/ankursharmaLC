# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:     
            while stack and stack[-1].val < head.val:
                stack.pop()
            stack.append(head)
            head = head.next 
        dummy = ListNode(0)
        curr = dummy
        for node in stack:
            curr.next = node
            curr = node
        curr.next = None  
        return dummy.next            