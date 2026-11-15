class Solution:
    def reverseString(self, s: list[str]) -> None:
        def helper(left,right):
            if left>=right: return 
            s[left],s[right]=s[right],s[left]
            helper(left+1,right-1)
        n=len(s)
        helper(0,n-1)
        
       

