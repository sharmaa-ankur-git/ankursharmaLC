class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n=len(arr)
        prev_no_del=arr[0]
        prev_one_del=float('-inf')
        result=arr[0]
        for i in range(1,n):
            x=arr[i]
            one_del=max(prev_no_del,prev_one_del+x)
            no_del=max(prev_no_del+x,x)            
            result=max(result,no_del,one_del)
            prev_no_del=no_del
            prev_one_del=one_del
        return result

        