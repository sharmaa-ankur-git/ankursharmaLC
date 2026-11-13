class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        count=0
        for ch in num:
            while stack and ch<stack[-1] and count<k:
                stack.pop()
                count+=1
            stack.append(ch)
        while count<k:
            stack.pop()
            count+=1
        return ''.join(stack).lstrip('0') or '0'
        