class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return True

        bracketMap = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:

            if char in bracketMap:
                topElement = stack.pop() if stack else '#'

                if bracketMap[char] !=topElement :
                    return False

            else:
                stack.append(char)

        return not stack 
        