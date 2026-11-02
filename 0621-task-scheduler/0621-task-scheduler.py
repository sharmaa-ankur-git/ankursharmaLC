from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count=Counter(tasks)
        max_heap=[-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        cooldown=[]
        time=0
        while max_heap or cooldown:
            time+=1
            still_cooling=[]
            for cnt,ready in cooldown:
                if ready==time:
                    heapq.heappush(max_heap,cnt)
                else:
                    still_cooling.append([cnt,ready])
            cooldown=still_cooling
            if max_heap:
                cnt=1+heapq.heappop(max_heap)
                if cnt!=0:
                    cooldown.append([cnt,time+n+1])
        return time


        
        