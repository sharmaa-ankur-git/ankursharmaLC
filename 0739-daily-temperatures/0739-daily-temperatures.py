class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        result=[0]*n
        t=temperatures
        for i in range(n-1,-1,-1):
            while stack and t[stack[-1]]<=t[i]:
                stack.pop()
            if stack:
                result[i]=abs(i-stack[-1])
            stack.append(i)
        return result


        