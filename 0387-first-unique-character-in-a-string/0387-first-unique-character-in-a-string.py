class Solution:
    def firstUniqChar(self, s: str) -> int:
        rack={}
        for char in s:
            rack[char]=rack.get(char,0)+1
        for i,char in enumerate(s):
            if rack[char]==1:
                return i
        return -1

        