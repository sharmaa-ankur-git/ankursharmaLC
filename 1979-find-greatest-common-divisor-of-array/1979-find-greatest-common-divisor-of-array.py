class Solution:
    def findGCD(self, nums: list[int]) -> int:
        mx=max(nums)
        mn=min(nums)
        while mn!=0:
            mx,mn=mn,mx%mn
        return mx
        