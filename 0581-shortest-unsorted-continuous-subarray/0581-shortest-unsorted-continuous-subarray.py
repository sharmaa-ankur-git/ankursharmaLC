class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        
        n=len(nums)
        low=0
        high=n-1
        while low<high and nums[low]<=nums[low+1]:
            low+=1
        if low==high:
            return 0
        while low<high and nums[high]>=nums[high-1]:
            high-=1
        sub_min=min(nums[low:high+1])
        sub_max=max(nums[low:high+1])
        while low>0 and nums[low-1]>sub_min:
            low-=1
        while high<n-1 and nums[high+1]<sub_max:
            high+=1
        return high-low+1