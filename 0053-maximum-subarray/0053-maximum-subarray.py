class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum=nums[0]
        current_num=nums[0]
        n=len(nums)
        max_sum=nums[0]
        for i in range(1,n):
            current_num=nums[i]
            current_sum=max(current_num,current_sum+current_num)
            max_sum=max(current_sum,max_sum)
        return max_sum