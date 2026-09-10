class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if not nums:
            return -1
        low,high =0,n-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid
        pivot=low
        if target>=nums[pivot] and target<=nums[n-1]:
            low,high=pivot,n-1
        else:
            low,high=0,pivot-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1
        
        