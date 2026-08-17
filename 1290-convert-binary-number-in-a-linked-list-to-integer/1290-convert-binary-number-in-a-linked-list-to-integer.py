# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        if head is None:
            return False
        bi=[]
        while head is not None:
            bi.append(head.val)
            head=head.next
        bi=bi[::-1]
        sum=0
        n=len(bi)
        for i in range(n):
            sum+=bi[i]*2**i
        return sum

