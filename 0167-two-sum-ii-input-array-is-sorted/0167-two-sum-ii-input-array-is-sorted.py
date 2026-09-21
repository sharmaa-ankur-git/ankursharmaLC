class Solution(object):
    def twoSum(self, numbers, target):
        n=len(numbers)
        nums=numbers
        low=0
        high=n-1
        while low<high:
            if nums[high]+nums[low]>target:
                high-=1
            elif nums[high]+nums[low]<target:
                low+=1
            else:
                return [low+1,high+1]
        return False
