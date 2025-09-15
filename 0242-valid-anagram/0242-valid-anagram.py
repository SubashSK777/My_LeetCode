class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return "".join(sorted(list(s))) == "".join(sorted(list(t)))