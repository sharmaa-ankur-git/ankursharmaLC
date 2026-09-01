class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        low=0
        longest=0
        freq={}

        for high in range(n):
            char=s[high]
            freq[char]=freq.get(char,0)+1
            max_freq=max(freq.values())
            window_len=high-low+1
            while window_len-max_freq>k:
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1
                window_len=high-low+1
                max_freq=max(freq.values())
            longest=max(longest,high-low+1)
        return longest
        