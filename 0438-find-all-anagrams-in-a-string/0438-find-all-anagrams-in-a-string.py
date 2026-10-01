class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p)>len(s):
            return []
        p_map={}
        for ch in p:
            p_map[ch]=p_map.get(ch,0)+1
        required=len(p_map)
        formed=0
        s_map={}
        low=0
        result=[]
        for high in range(len(s)):
            ch=s[high]
            s_map[ch]=s_map.get(ch,0)+1       
            if ch in p_map:
                if s_map[ch]==p_map[ch]:
                    formed+=1
                elif s_map[ch]==p_map[ch]+1:
                    formed-=1
            while high-low+1>len(p):
                left_ch=s[low]
                if left_ch in p_map:
                    if s_map[left_ch]==p_map[left_ch]:
                        formed-=1
                    elif s_map[left_ch]==p_map[left_ch]+1:
                        formed+=1
                s_map[left_ch]-=1
                low+=1
            if high-low+1==len(p) and formed==required:
                result.append(low)
        return result
    