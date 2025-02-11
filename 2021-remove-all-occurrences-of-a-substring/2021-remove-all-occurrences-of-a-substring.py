class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=''
        tz, pz=0, len(part)
        for c in s:
            stack+=c
            tz+=1
            if tz>=pz and stack.endswith(part):
                tz-=pz
                stack=stack[0:tz]
        return "".join(stack)