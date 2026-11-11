class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_close_map = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c not in open_close_map:
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] != open_close_map[c]:
                    return False
                stack.pop()
        return not stack