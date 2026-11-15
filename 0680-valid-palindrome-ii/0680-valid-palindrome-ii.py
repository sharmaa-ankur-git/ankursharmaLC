class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_valid(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                else:
                    left+=1
                    right-=1
            return True
        n=len(s)
        left=0
        right=n-1
        while left<right:
            if s[left]!=s[right]:
                if is_valid(left+1,right) or is_valid(left,right-1):
                    return True
                else:
                    return False
            else:
                left+=1
                right-=1
        return True
                

                


            
            