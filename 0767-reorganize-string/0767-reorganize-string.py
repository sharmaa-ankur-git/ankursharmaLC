from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        max_heap=[]
        counts=Counter(s)
        n=len(s)
        if max(counts.values()) > (n+1)//2:
            return ""           
        for ch,cnt in counts.items():
            heapq.heappush(max_heap,(-cnt,ch))
        result=[]
        prev_cnt,prev_ch=0," "
        while max_heap:
            cnt,ch=heapq.heappop(max_heap)
            result.append(ch)
            if prev_cnt<0:
                heapq.heappush(max_heap,(prev_cnt,prev_ch))
            prev_cnt=cnt+1
            prev_ch=ch
        return "".join(result)
