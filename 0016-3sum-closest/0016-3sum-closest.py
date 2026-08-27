class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        closest_diff = float('inf')   
        for i in range(n-2): 
            left = i + 1
            right = n - 1  
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                diff = target - curr_sum         
                if abs(diff) < abs(closest_diff):
                    closest_diff = diff
                    closest_sum = curr_sum            
                if diff > 0:  
                    left += 1
                elif diff < 0:  
                    right -= 1
                else: 
                    return curr_sum    
        return closest_sum