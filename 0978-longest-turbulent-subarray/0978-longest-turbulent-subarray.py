class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        n=len(arr)
        if n<2:
            return n
        max_len=1
        current_len=1
        prev_diff=0 
        for i in range(1,n):
            curr_diff=arr[i]-arr[i-1]
            if curr_diff==0:
                current_len=1
            elif (curr_diff>0 and prev_diff<0) or (curr_diff<0 and prev_diff>0):
                current_len+=1
            else:
                current_len=2
            max_len=max(max_len,current_len)
            prev_diff=curr_diff
        return max_len
    