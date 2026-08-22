class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_count={0:1}
        totsub_count=0
        current_sum=0
        n=len(nums)
        for i in range(n):
            num=nums[i]
            current_sum+=num
            remainder=current_sum%k
            if remainder in remainder_count:
                totsub_count+=remainder_count[remainder]
                remainder_count[remainder]+=1               
            else:
                remainder_count[remainder]=1
        return totsub_count
            

