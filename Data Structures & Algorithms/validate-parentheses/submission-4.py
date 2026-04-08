class Solution:
    def isValid(self, s: str) -> bool:
        size = len(s)
        if size % 2 != 0:
            return False

        stack = []

        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                last = stack.pop()
                if last == '[' and c == ']':
                    continue
                if last == '{' and c == '}':
                    continue
                if last == '(' and c == ')':
                    continue
                return False
        
        return len(stack) == 0
