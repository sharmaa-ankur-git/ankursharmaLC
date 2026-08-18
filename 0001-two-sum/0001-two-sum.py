class Solution(object):
    def twoSum(self, nums, target):   
        seen={}
        for i,num in enumerate(nums):
            val_req_for_tar=target-num
            if val_req_for_tar in seen:
                return(seen[val_req_for_tar],i)
            seen[num]=i
            