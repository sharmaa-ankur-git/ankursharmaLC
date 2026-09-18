class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def valid(capacity):
            total_weight=0
            day=1
            for weight in weights:
                total_weight+=weight
                if total_weight>capacity:
                    total_weight=weight
                    day+=1
                    if day>days:
                        return False
            return True
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(high+low)//2
            if valid(mid):
                high=mid
            else:
                low=mid+1
        return low

