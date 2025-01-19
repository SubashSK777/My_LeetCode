class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        return ' '.join(s)
        
        