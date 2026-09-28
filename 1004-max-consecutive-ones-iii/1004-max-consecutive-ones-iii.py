class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        low=0
        longest=0
        hash={0:0}
        for high in range(n):
            bd=nums[high]
            hash[bd]=hash.get(bd,0)+1
            while hash[0]>k:
                hash[nums[low]]-=1
                low+=1            
            longest=max(longest,high-low+1)
        return longest


