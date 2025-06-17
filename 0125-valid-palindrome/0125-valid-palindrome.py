class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l] != s[r]:
                return False

            r -= 1
            l += 1

        return True
            
            
