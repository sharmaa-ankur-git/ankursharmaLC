class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[]
        nums=nums*2
        for i in range(n):
            num=nums[i]
            found=False
            for j in range(i+1,2*n):
                if nums[j]>num:
                    result.append(nums[j])
                    found=True
                    break
                else:
                    continue
            if not found:
                result.append(-1)
        return result

       