class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesses = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in parenthesses:
                if not stack or parenthesses[char] != stack.pop():
                    return False
            else:
                stack.append(char)

        return not stack
