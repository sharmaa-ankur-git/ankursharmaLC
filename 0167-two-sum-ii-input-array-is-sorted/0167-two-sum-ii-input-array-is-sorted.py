class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums=numbers
        left=0
        n=len(numbers)
        right=n-1
        while left<right:
            summ=nums[left]+nums[right]
            if summ>target:
                right-=1
            elif summ<target:
                left+=1
            else:
                return [left+1,right+1]
        return False



