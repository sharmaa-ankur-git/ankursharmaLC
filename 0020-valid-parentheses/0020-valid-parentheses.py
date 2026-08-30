class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}       
        for char in s:
            if char in pairs:  
                stack.append(char)
            else: 
                if not stack or pairs[stack[-1]] != char:
                    return False
                stack.pop()       
        return not stack

        