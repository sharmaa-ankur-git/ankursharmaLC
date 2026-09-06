class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        n2=len(nums2)
        n1=len(nums1)
        for i in range(n1):
            num=nums1[i]
            idx=nums2.index(num)
            found=False
            for j in range(idx+1,n2):
                if nums2[j]>num:
                    result.append(nums2[j])
                    found=True
                    break
            if not found:
                result.append(-1)
        return result
            