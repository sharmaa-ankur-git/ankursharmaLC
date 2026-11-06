class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0])
        final=[intervals[0]]
        n=len(intervals)
        for i in range(1,n):
            if final[-1][1]>=intervals[i][0]:
                prev=final.pop()
                final.append([prev[0],max(intervals[i][1],prev[1])])
            else:
                final.append(intervals[i])
        return final
        


        