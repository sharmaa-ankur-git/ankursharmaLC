class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n=len(arr)
        prev_no_del=arr[0]
        prev_one_del=float("-inf")
        max_result=arr[0]
        for i in range(1,n):
            num=arr[i]
            no_del=max(prev_no_del+num,num)
            one_del=max(prev_no_del,prev_one_del+num)
            max_result=max(no_del,one_del,max_result)
            prev_no_del=no_del
            prev_one_del=one_del
        return max_result

        