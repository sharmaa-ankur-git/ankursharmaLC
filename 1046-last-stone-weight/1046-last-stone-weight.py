import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap=[]
        for weight in stones:
            heap.append(-weight)
        heapq.heapify(heap)
        while len(heap)>1:
            first=-heapq.heappop(heap)
            second=-heapq.heappop(heap)
            if first!=second:
                heapq.heappush(heap,-abs(first-second))
        return -heap[0] if heap else 0