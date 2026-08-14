class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prev_masum=nums[0]
        prev_misum=nums[0]
        max_sum=nums[0]
        min_sum=nums[0]
        n=len(nums)
        for i in range(1,n):
            current_num=nums[i]
            current_masum=max(prev_masum+current_num,current_num,prev_misum+current_num)
            current_misum=min(prev_masum+current_num,current_num,prev_misum+current_num)
            max_sum=max(current_masum,max_sum)
            min_sum=min(current_misum,min_sum)
            prev_masum=current_masum
            prev_misum=current_misum
        return max(max_sum,abs(min_sum))