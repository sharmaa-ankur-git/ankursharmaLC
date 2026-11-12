class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            num=nums[i]
            if num==0:
                nums[i]=-1
        max_len=0
        curr_sum=0
        sum_indices={0:-1}
        for i in range(n):
            num=nums[i]
            curr_sum+=num
            target=curr_sum
            if target in sum_indices:
                max_len=max(max_len,i-sum_indices[curr_sum])
            else:
                sum_indices[curr_sum]=i
        return max_len
        