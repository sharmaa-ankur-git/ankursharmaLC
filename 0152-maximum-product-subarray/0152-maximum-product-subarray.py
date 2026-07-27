class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            current_max = max_product
            current_min = min_product
            max_product = max(num, current_max * num, current_min * num)
            min_product = min(num, current_max * num, current_min * num)
            
            result = max(result, max_product)
        
        return result
        