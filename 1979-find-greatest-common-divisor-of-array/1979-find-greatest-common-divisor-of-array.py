class Solution:
    def findGCD(self, nums: list[int]) -> int:
        mx=max(nums)
        mn=min(nums)
        def hcf(mx,mn):
            if mn==0: return mx
            mx,mn=mn,mx%mn
            return hcf(mx,mn)
        return hcf(mx,mn)