class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n=len(nums)
        for i in range(n):
            nums[i]=nums[i]**2
        nums.sort()
        return nums