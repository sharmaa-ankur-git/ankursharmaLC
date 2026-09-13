class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)<m*k:
            return -1
        def canmake(days:int):
            flower=0
            bouquet=0
            for bloom in bloomDay:
                if bloom<=days:
                    flower+=1
                    if flower==k:
                        bouquet+=1
                        flower=0
                else:
                    flower=0
            return bouquet>=m
        #hum binary search is used
        left,right=min(bloomDay),max(bloomDay)
        ans=-1
        while left<right:
            mid=(left+right)//2
            if canmake(mid):
                right=mid
            else:
                left=mid+1
        return left
        
        