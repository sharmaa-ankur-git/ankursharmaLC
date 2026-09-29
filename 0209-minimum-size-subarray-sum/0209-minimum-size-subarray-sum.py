class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        shortest=float('inf')
        n=len(nums)
        low=0
        curr_sum=0
        for high in range(n):
            num=nums[high]
            curr_sum+=num
            while curr_sum>=target:
                curr_sum-=nums[low]
                shortest=min(shortest,high-low+1)
                low+=1
        if shortest==float('inf'):
            return 0
        else:
            return shortest