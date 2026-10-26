class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            elif c == "}":
                if len(stack) == 0:
                    return False
                if stack.pop() != "{":
                    return False
            elif c == ")":
                if len(stack) == 0:
                    return False
                if stack.pop() != "(":
                    return False
            elif c == "]":
                if len(stack) == 0:
                    return False
                if stack.pop() != "[":
                    return False
        return len(stack) == 0