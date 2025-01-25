class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""

        for i in s:
            if i.isalnum():
                s1 += i.lower()

        l = 0
        r = len(s1) - 1

        while l < r:
            if s1[l] == s1[r]:
                l += 1
                r -= 1
            else:
                return False
        return True



        