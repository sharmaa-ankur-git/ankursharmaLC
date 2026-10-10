from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s1_map=Counter(s)
        s2_map=Counter(t)
        common=0
        for char in s1_map:
            if char in s2_map:
                common+=min(s2_map[char],s1_map[char])
        total_steps=len(s)-common
        return total_steps

        
        