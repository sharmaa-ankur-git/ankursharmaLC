class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        chars=list(text)
        count=0                               #still unatural way to do it for me
        while True:
            for char in "balloon":
                if char in chars:              
                    chars.remove(char)
                else:
                    return count
            count+=1
        