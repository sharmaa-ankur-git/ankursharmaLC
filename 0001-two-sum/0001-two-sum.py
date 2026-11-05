class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for i,num in enumerate(nums):
            req=target-num
            if req in seen:
                return [seen[req],i]
            seen[num]=i
        return []