from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_freq=Counter(s)
        for ch in t:
            if ch in s_freq:
                s_freq[ch]-=1
                if s_freq[ch]==0:
                    del s_freq[ch]
            else:
                return False
        return False if s_freq else True