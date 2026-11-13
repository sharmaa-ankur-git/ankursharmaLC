class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nex_grea={}  #dict to store next greater element for the particular element
        stack=[]
        for num in nums2[::-1]:
            while stack and stack[-1]<=num:
                stack.pop()
            if stack:
                nex_grea[num]=stack[-1]
            else:
                nex_grea[num]=-1
            stack.append(num)
        return [nex_grea[num] for num in nums1]
        