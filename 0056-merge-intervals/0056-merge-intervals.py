class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        for start, end in intervals:
            if res and start <= last_end:
                new_end = max(last_end,end)
                res[-1][1] = new_end
                last_end = new_end
            else:
                res.append([start,end])
                last_end = end
        return res
        