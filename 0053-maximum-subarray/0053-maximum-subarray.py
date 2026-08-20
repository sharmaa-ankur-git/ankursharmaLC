class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        current_max=nums[0]
        max_sum=nums[0]
        result=0
        for i in range(1,n):
            num=nums[i]         
            current_max=max(current_max+num,num)
            max_sum=max(max_sum,current_max)         
        return max_sum
        

        