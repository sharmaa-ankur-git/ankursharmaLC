class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_len=0
        max_unique=len(set(s))
        for target_unique in range(1,max_unique+1):
            freq={}
            left=0
            unique_count=0
            count_at_least_k=0
            for right in range(len(s)):
                char_r=s[right]
                if freq.get(char_r,0)==0:
                    unique_count+=1
                freq[char_r]=freq.get(char_r,0)+1
                if freq[char_r]==k:
                    count_at_least_k+=1
                while unique_count>target_unique:
                    char_l=s[left]
                    if freq[char_l]==k:
                        count_at_least_k-=1
                    freq[char_l]-=1
                    if freq[char_l]==0:
                        unique_count-=1
                    left+=1
                if unique_count==target_unique==count_at_least_k:
                    max_len=max(max_len,right-left+1)  
        return max_len


        