class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        current_sum = 0
        subarray_count = 0   
        n=len(nums)   
        for i in range(n):
            current_sum += nums[i]
            target=current_sum-k      
            if target in prefix_count:
                subarray_count+=prefix_count[target]
            if current_sum in prefix_count:
                prefix_count[current_sum]+=1
            else:
                prefix_count[current_sum]=1
        return subarray_count




        