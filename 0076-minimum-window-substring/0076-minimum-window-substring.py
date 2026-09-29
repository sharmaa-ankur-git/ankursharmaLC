class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s)<len(t):
            return ""
        min_len=float('inf')
        t_dict={}
        for char in t:
            t_dict[char]=t_dict.get(char,0)+1
        required=len(t_dict)
        formed=0
        s_map={}
        low=0
        n=len(s)
        best_win=(0,0)
        for high in range(n):
            char=s[high]
            s_map[char]=s_map.get(char,0)+1
            if char in t_dict and t_dict[char]==s_map[char]:
                formed+=1
            while formed==required:
                curr_len=high-low+1
                if curr_len<min_len:
                    min_len=curr_len
                    best_win=(low,high)
                s_map[s[low]]-=1
                if s[low] in t_dict and s_map[s[low]]<t_dict[s[low]]:
                    formed-=1 
                low+=1
        return "" if min_len==float('inf') else s[best_win[0]:best_win[1]+1]
        