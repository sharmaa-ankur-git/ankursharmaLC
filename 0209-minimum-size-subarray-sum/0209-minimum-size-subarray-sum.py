class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        window_sum=0
        min_len=float("inf")
        low=0
        for high in range(n):
            if window_sum<target:
                window_sum+=nums[high]
            while window_sum>=target:
                min_len=min(min_len,high-low+1)
                window_sum-=nums[low]
                low+=1
        if min_len==float("inf"):
            return 0
        else:
            return min_len        
