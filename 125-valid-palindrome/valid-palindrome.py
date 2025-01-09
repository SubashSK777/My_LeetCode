class Solution:
    def isPalindrome(self, s: str) -> bool:
        res_str = ""

        for c in s:
            if c.isalnum():
                res_str += c.lower()
        return res_str == res_str[::-1]

        