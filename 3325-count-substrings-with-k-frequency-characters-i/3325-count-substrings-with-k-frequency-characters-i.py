from collections import Counter
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        freq = Counter()
        ans=0
        left=0  
        for right,char in enumerate(s):
            freq[char]+=1
            while freq[char]>=k:
                freq[s[left]]-=1
                left+=1
            ans+=left
            
        return ans
        