class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       nums=list(reversed(sorted(nums)))
       num=nums[k-1]
       return num

        