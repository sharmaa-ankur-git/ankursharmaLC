class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        hash={}
        low=0
        win_len=float("-inf")
        for high in range(n):
            char=s[high]
            hash[char]=hash.get(char,0)+1
            while hash[char]>1:
                hash[s[low]]-=1
                low+=1
            if high-low+1>win_len:
                win_len=high-low+1
        return 0 if win_len==float("-inf") else win_len
        