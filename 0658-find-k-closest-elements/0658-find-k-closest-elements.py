import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            diff_num = (-abs(num - x),-num)
            if len(heap)<k:
                heapq.heappush(heap,diff_num)
            else:
                heapq.heappushpop(heap,diff_num)
        return sorted([-num for diff,num in heap])
        