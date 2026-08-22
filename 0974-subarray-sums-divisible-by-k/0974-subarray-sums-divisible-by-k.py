class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_count={0:1}
        totsub_count=0
        current_sum=0
        n=len(nums)
        for num in nums:
            current_sum+=num
            remainder=current_sum%k
            totsub_count+=remainder_count.get(remainder,0)
            remainder_count[remainder]=remainder_count.get(remainder,0)+1
        return totsub_count
            

