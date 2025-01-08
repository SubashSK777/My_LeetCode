class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        length = len(words)

        for i in range (length):
            n = len(words[i])
            for j in range (i,length):
                if i != j:
                    if words[i] == words[j][:n] and words[i] == words[j][-n:]:
                        count += 1
        return count
        