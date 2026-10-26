import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        n=len(points)
        heap=[]
        for x,y in points:
            dist=-(x**2 + y**2)
            if len(heap)<k:
                heapq.heappush(heap,(dist,x,y))
            else:
                heapq.heappushpop(heap,(dist,x,y))
        return [[x,y] for dist,x,y in heap]

        