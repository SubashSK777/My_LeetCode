class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        res = s.strip().split(" ")
        
        return len(res[-1])
        