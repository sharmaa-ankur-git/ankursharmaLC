class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current_max=nums[0]
        max_sum=nums[0]
        current_min=nums[0]
        min_sum=nums[0]
        n=len(nums)
        total_sum=sum(nums)
        for i in range(1,n):
            current_num=nums[i]
            current_max=max(current_max+current_num,current_num)
            current_min=min(current_min+current_num,current_num)
            max_sum=max(current_max,max_sum)
            min_sum=min(current_min,min_sum)
        if max_sum<0:
            return max_sum
        return max(max_sum,total_sum-min_sum)

        