class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_map = {')': '(', ']':'[', '}' : '{'}
        for c in s:
            if c in close_map:
                if stack and close_map[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack