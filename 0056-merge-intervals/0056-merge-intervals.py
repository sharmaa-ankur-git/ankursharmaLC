class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = True      
        while merged:
            merged = False
            n = len(intervals)
            for i in range(n):
                for j in range(i + 1, n):
                    if not (intervals[i][1] < intervals[j][0] or intervals[j][1] < intervals[i][0]):
                        new_interval = [min(intervals[i][0], intervals[j][0]),max(intervals[i][1], intervals[j][1])]
                        intervals.pop(j)
                        intervals.pop(i)
                        intervals.append(new_interval)
                        merged = True
                        break
                if merged:
                    break
        return intervals
        