class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        stack=[]
        nextwarmdaycount={}
        for i in range(n-1,-1,-1):
            temp=temperatures[i]
            days=1
            while stack and stack[-1][0]<=temp:
                prev_temp,prev_days=stack.pop()
                days+=prev_days
            nextwarmdaycount[i]= days if stack else 0
            stack.append((temp,days))
        return [nextwarmdaycount[i] for i in range(n)]

        