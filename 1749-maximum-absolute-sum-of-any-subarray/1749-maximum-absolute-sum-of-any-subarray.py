class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        currentMsum=nums[0]
        currentmsum=nums[0]
        max_sum=nums[0]
        min_sum=nums[0]
        result=max(max_sum,abs(min_sum))
        for i in range(1,n):
            current_num=nums[i]
            currentMsum=max(current_num,current_num+currentMsum)
            currentmsum=min(current_num,current_num+currentmsum)
            max_sum=max(currentMsum,max_sum)
            min_sum=min(currentmsum,min_sum) 
            result=max(max_sum,abs(min_sum),result)          
        return result
        


        