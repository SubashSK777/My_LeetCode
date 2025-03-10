class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set("aeiou")
        n = len(word)
        result = 0
         # Precompute next_consonant: for every index, store the next index where a consonant occurs.
        next_consonant = [n] * n
        next_cons_index = n
        for i in range(n - 1, -1, -1):
            next_consonant[i] = next_cons_index
            if word[i] not in vowels:
                next_cons_index = i

        vowel_count = {}
        cons_count = 0
        left = 0  # left pointer for the sliding window

        for right in range(n):
            ch = word[right]
            if ch in vowels:
                vowel_count[ch] = vowel_count.get(ch, 0) + 1
            else:
                cons_count += 1

            # If too many consonants, shrink from the left.
            while cons_count > k and left <= right:
                left_ch = word[left]
                if left_ch in vowels:
                    vowel_count[left_ch] -= 1
                    if vowel_count[left_ch] == 0:
                        del vowel_count[left_ch]
                else:
                    cons_count -= 1
                left += 1

            # When the current window has exactly k consonants and contains all vowels,
            # count all valid substrings formed by extending the window with following vowels.
            while left <= right and cons_count == k and len(vowel_count) == 5:
                # All substrings from current valid window ending at 'right' and extending till
                # right before the next consonant are valid.
                result += next_consonant[right] - right

                # Move left pointer to try for a new valid window.
                left_ch = word[left]
                if left_ch in vowels:
                    vowel_count[left_ch] -= 1
                    if vowel_count[left_ch] == 0:
                        del vowel_count[left_ch]
                else:
                    cons_count -= 1
                left += 1

        return result