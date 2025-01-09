class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = ""

        min_len = min(len(word1), len(word2))

        for i in range (0, min(len(word1), len(word2))):
            res += word1[i]
            res += word2[i]

        res += word1[min_len:]
        res += word2[min_len:]

        return res


        