class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_count = {0: 1}       
        current_sum = 0
        total_subarrays = 0        
        for num in nums:
            current_sum += num           
            remainder = current_sum % k           
            if remainder in remainder_count:
                total_subarrays += remainder_count[remainder]
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1               
        return total_subarrays
        
        
        

