class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        count = 0
        i = 0 
        j = 0

        if len(s) == 0:
            return True

        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i += 1
                j += 1
                count += 1
            else:
                j += 1

        return (count >= len(s))
        