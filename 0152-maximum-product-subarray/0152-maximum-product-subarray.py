class Solution(object):
    def maxProduct(self, nums):
        n=len(nums)
        current_num=nums[0]
        max_product=nums[0]
        min_product=nums[0]
        best_prod=nums[0]
        for i in range(1,n):
            current_nums=nums[i]
            current_max=max_product
            current_min=min_product
            min_product=min(current_max*current_nums,current_nums,current_min*current_nums)
            max_product=max(current_max*current_nums,current_nums,current_min*current_nums)
            best_prod=max(max_product,best_prod)
        return best_prod
