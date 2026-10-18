class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        min_sum=nums[0]
        max_sum=nums[0]
        curr_max=nums[0]
        curr_min=nums[0]
        n=len(nums)
        for i in range(1,n):
            curr_num=nums[i]
            curr_max=max(curr_num,curr_max+curr_num)
            curr_min=min(curr_num,curr_min+curr_num)
            max_sum=max(curr_max,max_sum)
            min_sum=min(curr_min,min_sum)           
        if max_sum<0:
            return max_sum
        return max(max_sum,total_sum-min_sum)
        
        
        