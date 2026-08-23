class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        current_sum=0
        sum_indices={0:-1}
        max_len=0

        for i,num in enumerate(nums):
            if num==0:
                current_sum+=1
            else:
                current_sum-=1
            if current_sum in sum_indices:
                max_len=max(max_len,i-sum_indices[current_sum])
            else:
                sum_indices[current_sum]=i
        return max_len