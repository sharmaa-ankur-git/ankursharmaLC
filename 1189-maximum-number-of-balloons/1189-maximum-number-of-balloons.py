class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        chars=list(text)
        count=0
        while True:
            for char in "balloon":
                if char in chars:
                    chars.remove(char)
                else:
                    return count
            count+=1
        