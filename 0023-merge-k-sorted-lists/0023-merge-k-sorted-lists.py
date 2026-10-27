# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        vals=[]  
        for node in lists:
            while node:
                vals.append(node.val)
                node=node.next         
        vals.sort()    
        dummy=ListNode(0)
        tail=dummy
        for v in vals:
            tail.next=ListNode(v)
            tail=tail.next      
        return dummy.next       