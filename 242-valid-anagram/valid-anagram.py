class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = sorted(list(s))
        list_t = sorted(list(t))
        
        if len(s) == len(t):
            if list_s == list_t:
                return True
        return False
