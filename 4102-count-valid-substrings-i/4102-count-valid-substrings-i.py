class Solution:
    def countValidSubstrings(self, s: str) -> int:
        count=0
        n=len(s)
        j=0
        for i in range(n):
            if i>=2 and s[i-2:i+1]=="abc":
                j=i-1
            count+=i-j+1
        return count
        