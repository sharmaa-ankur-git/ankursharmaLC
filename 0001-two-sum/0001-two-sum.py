class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pairs=[]
        for i,num in enumerate(nums):
            pairs.append([num,i])
        pairs.sort()
        n=len(pairs)
        right,left=n-1,0
        while left<right:
            summ=pairs[left][0]+pairs[right][0]
            if summ>target:
                right-=1
            elif summ<target:
                left+=1
            else:
                return [pairs[left][1],pairs[right][1]]
        return []
        