class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num:int) ->int:
            total_sum=0
            while num>0:
                digit=num%10
                total_sum+=digit**2
                num=num//10
            return total_sum
        slow=n
        fast=get_next(n)
        while fast!=1 and fast!=slow:
            slow=get_next(slow)
            fast=get_next(get_next(fast))    
        return fast==1    
        