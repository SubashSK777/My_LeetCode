class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = defaultdict(int)

        for i in s:
            res[i] += 1

        for i in t:
            res[i] -= 1

        for val in res.values():
            if val != 0:
                return False
        return True
        