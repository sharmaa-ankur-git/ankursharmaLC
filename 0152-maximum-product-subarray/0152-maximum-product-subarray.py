class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_num=nums[0]
        n=len(nums)
        current_max=nums[0]
        current_min=nums[0]
        max_result=nums[0]
        for i in range(1,n):
            current_num=nums[i]
            max_prod=max(current_max*current_num,current_num,current_min*current_num)
            min_prod=min(current_max*current_num,current_num,current_min*current_num)
            max_result=max(max_prod,min_prod,max_result)
            current_max=max_prod
            current_min=min_prod
        return max_result
