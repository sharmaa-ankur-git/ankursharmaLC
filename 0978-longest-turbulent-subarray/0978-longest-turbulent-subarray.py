class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        n=len(arr)
        if n<2:
            return n
        max_len=1
        curr_len=1
        prev_diff=0
        for i in range(1,n):
            curr_diff=arr[i]-arr[i-1]
            if curr_diff==0:
                curr_len=1
            elif (prev_diff>0 and curr_diff<0) or (prev_diff<0 and curr_diff>0):
                curr_len+=1
            else:
                curr_len=2
            max_len=max(max_len,curr_len)
            prev_diff=curr_diff
        return max_len
        