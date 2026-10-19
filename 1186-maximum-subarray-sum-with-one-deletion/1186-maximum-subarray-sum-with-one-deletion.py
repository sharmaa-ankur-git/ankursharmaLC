class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        n=len(arr)
        no_del=arr[0]
        one_del=float("-inf")
        max_sum=arr[0]
        for i in range(1,n):
            num=arr[i]
            one_del=max(no_del,one_del+num)
            no_del=max(num,no_del+num)
            max_sum=max(one_del,no_del,max_sum)
        return max_sum