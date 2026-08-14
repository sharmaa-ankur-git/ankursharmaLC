class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n=len(arr)
        no_del=arr[0]
        one_del=float('-inf')
        result=arr[0]
        for i in range(1,n):
            x=arr[i]
            prev_no_del=no_del
            prev_one_del=one_del
            one_del=max(prev_no_del,prev_one_del+x)
            no_del=max(prev_no_del+x,x)            
            result=max(result,no_del,one_del)           
        return result

        