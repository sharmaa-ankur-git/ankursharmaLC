class Solution:
    def isHappy(self, n: int) -> bool:
        def nex_num(num):
            total=0
            while num>0:
                digit=num%10
                total+=digit**2
                num=num//10
            return total
        slow=n
        fast=nex_num(n)
        while fast!=1 and slow!=fast:
            slow=nex_num(slow)
            fast=nex_num(nex_num(fast))
        return fast==1

        