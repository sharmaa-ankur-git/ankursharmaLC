# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        val_list=[]
        while head!=None:
            val_list.append(head.val)
            head=head.next
        result=0
        for i in range(len(val_list)):
            result+=(2**(len(val_list)-1-i)) * val_list[i]
        return result



        