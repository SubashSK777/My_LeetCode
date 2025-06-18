class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = {}

        for i in range(len(s)):
            if s[i] in hm:
                hm[s[i]] += 1
            else:
                hm[s[i]] = 1

        for i in range(len(s)):
            if hm[s[i]] == 1:
                return i

        return -1