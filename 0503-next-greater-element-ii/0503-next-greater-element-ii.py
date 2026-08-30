class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n      
        for i in range(n):
            for j in range(1, n):
                next_idx = (i + j) % n
                if nums[next_idx] > nums[i]:
                    result[i] = nums[next_idx]
                    break                   
        return result