class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {'(':')' , '[':']' , '{' : '}' }

        for i in s:
            if i in map:
                stack.append(i)

            elif len(stack) == 0 or map[stack.pop()] != i:
                return False

        return len(stack) == 0
                