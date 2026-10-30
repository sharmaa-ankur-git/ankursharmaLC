import heapq
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n=len(matrix)
        m=len(matrix[0])
        heap=[]
        for r in range(n):
            heap.append((matrix[r][0],r,0))
        heapq.heapify(heap)
        for r in range(k):
            val,r,c=heapq.heappop(heap)  
            if c+1<m:
                heapq.heappush(heap,(matrix[r][c+1],r,c+1))
        return val
        