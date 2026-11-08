class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        n=len(s)
        for i in range(n):
            char=s[i]
            if stack and char==stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

        