import heapq
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n=len(matrix)
        heap=[]
        for _ in range(n):
            heap.append((matrix[_][0], _, 0))
        heapq.heapify(heap)
        for _ in range(k):
            val,_,c=heapq.heappop(heap)  
            if c+1<n:
                heapq.heappush(heap,(matrix[_][c+1],_,c+1))
        return val
        