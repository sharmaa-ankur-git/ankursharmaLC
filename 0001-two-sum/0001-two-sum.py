class Solution(object):
    def twoSum(self, nums, target):   
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                sum=nums[i]+nums[j]
                if sum==target:
                    return(i,j)
                else:
                    continue