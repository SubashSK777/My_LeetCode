class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mini = min(len(word1), len(word2))

        res = []
        for i in range(mini):
            res.append(word1[i])
            res.append(word2[i])
        
        res.append(word1[mini:])
        res.append(word2[mini:])
        
        return (''.join(res))