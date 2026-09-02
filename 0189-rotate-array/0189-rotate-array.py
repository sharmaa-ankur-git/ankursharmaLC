class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        left=0
        right=n-1
        def reverse(left,right):   
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
            return nums
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        return nums
        