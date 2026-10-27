import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap=[]   
        for i,row in enumerate(mat):
            strength=sum(row) 
            heapq.heappush(heap, (strength, i))
        result=[]
        for i in range(k):
            strength,idx=heapq.heappop(heap)
            result.append(idx)       
        return result
        