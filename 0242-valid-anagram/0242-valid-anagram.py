class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        n=len(s)
        track={}
        
        for char in s:
            track[char]=track.get(char,0)+1
        for char in t:
            track[char]=track.get(char,0)-1
            if track[char]<0:
                return False
        return True
        