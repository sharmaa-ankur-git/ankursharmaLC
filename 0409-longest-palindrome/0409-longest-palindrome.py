from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts=Counter(s)
        count=0
        is_odd=False
        for c in counts.values():
            count+=(c//2)*2
            if c%2==1:
                is_odd=True
        return count+1 if is_odd else count


        