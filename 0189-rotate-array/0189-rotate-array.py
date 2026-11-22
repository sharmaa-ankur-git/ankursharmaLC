class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        numl=nums[::-1]
        numl=numl[:k][::-1]+numl[k:][::-1]
        nums[:]=numl
        