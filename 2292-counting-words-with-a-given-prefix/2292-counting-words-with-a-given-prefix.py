class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        len_pref = len(pref)
        count = 0

        for i in words:
            if pref in i[:len_pref]:
                count += 1
        return count

        