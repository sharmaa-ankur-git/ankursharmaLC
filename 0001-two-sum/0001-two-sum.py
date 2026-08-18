class Solution(object):
    def twoSum(self, nums, target):
        sum=0
        n=len(nums)
        left=0
        right=n-1
        
        for i in range(n):
            for j in range(i+1,n):
                sum=nums[i]+nums[j]
                if sum==target:
                    return(i,j)
                else:
                    continue