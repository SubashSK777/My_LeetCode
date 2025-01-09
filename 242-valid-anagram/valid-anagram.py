class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = sorted(s)
        t_set = sorted(t)

        if s_set == t_set:
            return True
        else:
            return False
        