class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closings = {')' : '(', ']' : '[', '}': '{' }
        for c in s:
            if not stack and c in closings:
                return False
            else:
                if c not in closings:
                    stack.append(c)
                elif closings[c] == stack[-1]:
                        stack.pop()
                else:
                    stack.append(c)
        return len(stack) == 0
