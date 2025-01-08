class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        a = len(word1)
        b = len(word2)
        n = min(a,b)
        out = ""

        for i in range(n):
            out += word1[i] + word2[i]

        if a > b:
            out += word1[n:]
        else:
            out += word2[n:]
            
        return out
        