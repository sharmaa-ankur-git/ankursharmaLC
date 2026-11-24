import math
class Solution:
    def findGCD(self, nums: list[int]) -> int:
        gcd_val=math.gcd(max(nums),min(nums))
        return gcd_val
        