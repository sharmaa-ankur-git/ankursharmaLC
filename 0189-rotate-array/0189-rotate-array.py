class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        f_port=nums[0:n-k]
        l_port=nums[n-k:]
        nums[:]=l_port+f_port
        