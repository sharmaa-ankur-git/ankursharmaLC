from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if nums is None:
            return None
        freq=Counter(nums)
        n=len(freq)
        for key,value in freq.items():
            if freq[key]>1:
                return key
        return None       
             
            

        