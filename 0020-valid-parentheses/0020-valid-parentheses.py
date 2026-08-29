class Solution:
    def isValid(self, s: str) -> bool:   
        stack = []
        bracket_pairs = {')': '(', '}': '{', ']': '['}        
        for char in s:
            if char in bracket_pairs: 
                if not stack or stack[-1] != bracket_pairs[char]:
                    return False
                stack.pop()
            else: 
                stack.append(char)       
        return len(stack) == 0
        