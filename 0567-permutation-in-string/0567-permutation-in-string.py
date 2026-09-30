class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_map={}
        for ch in s1:
            s1_map[ch]=s1_map.get(ch,0)+1
        required=len(s1_map)
        formed=0
        s2_map={}
        low=0 
        for high in range(len(s2)):
            ch=s2[high]
            s2_map[ch]=s2_map.get(ch,0)+1
            if ch in s1_map:
                if s2_map[ch]==s1_map[ch]:
                    formed+=1
                elif s2_map[ch]==s1_map[ch]+1:
                    formed-=1
            if high-low+1>len(s1):
                left_ch=s2[low]
                if left_ch in s1_map:
                    if s2_map[left_ch]==s1_map[left_ch]:
                        formed-=1
                    elif s2_map[left_ch]==s1_map[left_ch]+1:
                        formed+=1
                s2_map[left_ch]-=1
                low+=1
            if high-low+1==len(s1) and formed==required:
                return True
        return False