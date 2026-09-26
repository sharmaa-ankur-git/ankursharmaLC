class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stackfun(string):
            stack=[]
            for ch in string:
                if ch=="#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return "".join(stack)
        return stackfun(s)==stackfun(t)
                    

        