class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        closest_diff=float("inf")
        closest_sum=float("inf")
        for i in range(n-2):
            low=i+1
            high=n-1
            while low<high:
                current_sum=nums[high]+nums[low]+nums[i]
                diff=current_sum-target
                if abs(diff)<abs(closest_diff):
                    closest_diff=diff
                    closest_sum=current_sum
                if diff>0:
                    high-=1
                elif diff<0:
                    low+=1
                else:
                    return current_sum
        return closest_sum
                



        