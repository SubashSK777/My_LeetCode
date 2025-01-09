class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        n = len(pref)

        for i in words:
            if pref in i[:n]:
                count += 1

        return count