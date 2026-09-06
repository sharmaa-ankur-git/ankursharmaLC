class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        nxt_greater={}
        for num in nums2:
            while stack and num>stack[-1]:
                smaller=stack.pop()
                nxt_greater[smaller]=num
            stack.append(num)
        return [nxt_greater.get(x, -1) for x in nums1]
        