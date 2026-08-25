class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged=True
        while merged:
            merged=False
            for i in range(1,len(intervals)):
                if intervals[i-1][1]>=intervals[i][0]:
                    start=intervals[i-1][0]
                    end=max(intervals[i][1],intervals[i-1][1])
                    new_interval=[start,end]
                    intervals.pop(i)
                    intervals.pop(i-1)
                    intervals.insert(i-1,new_interval)
                    intervals.sort(key=lambda x:x[0])
                    merged=True
                    break
                else:
                    continue
        return intervals
        