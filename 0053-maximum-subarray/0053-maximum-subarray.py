class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum=nums[0]
        curr_sum=nums[0]
        n=len(nums)
        for i in range(1,n):
           curr_num=nums[i]
           curr_sum=max(curr_num+curr_sum,curr_num)
           max_sum=max(curr_sum,max_sum)
        return max_sum
           