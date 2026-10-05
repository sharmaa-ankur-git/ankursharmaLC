class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        result=[]
        n=len(nums)
        low=0
        curr_sum=sum(nums[0:k])
        for high in range(k-1,n):
            if high>=k:
                curr_sum+=nums[high]-nums[low]
                low+=1
            avg=curr_sum/float(k)
            result.append(avg)
        return max(result)
            
        