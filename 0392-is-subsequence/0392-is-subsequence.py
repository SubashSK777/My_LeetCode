class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        count = 0

        for j in range(len(t)):
            if i == len(s):
                return True

            if s[i] == t[j]:
                i += 1
                count += 1

        return (count >= len(s))
        