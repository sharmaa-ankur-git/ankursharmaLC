class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.lower()
        cleaned="".join(char for char in s if char.isalnum())
        if cleaned==cleaned[::-1]:
            return True
        else:
            return False