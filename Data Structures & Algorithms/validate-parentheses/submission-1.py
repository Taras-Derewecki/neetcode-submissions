class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) > 1:
                if i == ")" and stack[-2] == "(":
                    stack.pop()
                    stack.pop()
                if i == "]" and stack[-2] == "[":
                    stack.pop()
                    stack.pop()
                if i == "}" and stack[-2] == "{":
                    stack.pop()
                    stack.pop()

        if not stack:
            return True
        return False
