class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        result=[]
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue    #to handle outer duplicate element because they would be same 
            low=i+1
            high=n-1
            while low<high:
                sum=nums[i]+nums[low]+nums[high]
                if sum<0:
                    low+=1
                elif sum>0:
                    high-=1
                else:
                    result.append([nums[i],nums[low],nums[high]])
                    #below this to handle inner duplicates 
                    while low<high and nums[low]==nums[low+1]:
                        low+=1
                    while low<high and nums[high]==nums[high-1]:
                        high-=1
                    low+=1
                    high-=1
        result
        seen=set()
        res=[x for x in result if not(tuple(x) in seen or seen.add(tuple(x)))]
        return res

        
        
        