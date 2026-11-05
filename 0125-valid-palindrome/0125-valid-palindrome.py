class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        string=[]
        for ch in s:
            if ch.isalnum():
                string.append(ch)
        return string==string[::-1]
        