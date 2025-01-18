class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 +str1:
            return ""

        bige = str1 + str2
        n = gcd(len(str1), len(str2))

        return bige[:n]