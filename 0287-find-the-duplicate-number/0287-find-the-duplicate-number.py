class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        seen={}
        for i in range(n):
            num=nums[i]
            seen[num]=seen.get(num,0)+1
            if seen[num]==2:
                return num
        