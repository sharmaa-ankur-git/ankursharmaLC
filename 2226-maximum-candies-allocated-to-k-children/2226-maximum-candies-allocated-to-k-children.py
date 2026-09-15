class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n=len(candies)
        total=sum(candies)
        if total<k:
            return 0 
        low=1
        high=total//k
        while low<high:
            mid=(low+high+1)//2
            count=sum(c//mid for c in candies)
            if count>=k:
                low=mid
            else:
                high=mid-1
        return low
        