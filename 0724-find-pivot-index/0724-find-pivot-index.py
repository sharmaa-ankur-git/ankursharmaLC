class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        total_sum=sum(nums)
        for i in range(n):
            left_sum=sum(nums[0:i])
            right_sum=total_sum-left_sum-nums[i]
            if right_sum==left_sum:
                pivot_index=i
                return pivot_index
        return -1









        