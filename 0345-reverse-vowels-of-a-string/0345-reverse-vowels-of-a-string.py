class Solution:
    def reverseVowels(self, s: str) -> str:

        vowel = []

        for char in s:
            if char in "aeiouAEIOU":
                vowel.append(char)

        vowel.reverse()
        result = []
        vow_count = 0

        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                result.append(vowel[vow_count])
                vow_count += 1
            else:
                result.append(s[i])

        return ''.join(result)


        