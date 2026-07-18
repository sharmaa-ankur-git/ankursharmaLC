class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        z_count=0
        n=len(nums)
        longest=0
        low=0
        for high in range(n):
            if nums[high]==0:
                z_count+=1
            while z_count>k:
                if nums[low]==0:
                    z_count-=1
                low+=1
            window_len=high-low+1  
            longest=max(window_len,longest)
        return longest
    

        

            


        



