class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        curr_min=nums[0]
        curr_max=nums[0]
        curr_prod=nums[0]
        n=len(nums)
        result=nums[0]
        for i in range(1,n):
            curr_num=nums[i]
            temp_max=max(curr_max*curr_num,curr_num,curr_min*curr_num)
            curr_min=min(curr_min*curr_num,curr_num,curr_max*curr_num)
            curr_max=temp_max
            max_prod=max(curr_num,curr_min,curr_max)
            result=max(result,max_prod)
        return result



        