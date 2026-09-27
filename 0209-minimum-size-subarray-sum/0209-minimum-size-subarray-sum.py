class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        result=[]
        curr_sum=0
        n=len(nums)
        low=0
        for high in range(n):
                curr_sum+=nums[high]
                while curr_sum>=target:
                    result.append(high-low+1)
                    curr_sum-=nums[low]
                    low+=1                
        if result:
            return min(result)
        else:
            return 0
        