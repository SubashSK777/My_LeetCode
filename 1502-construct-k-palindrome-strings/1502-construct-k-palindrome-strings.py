from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        count = 0
        if len(s) < k:
            return False
        s_map = Counter(s)

        for i in s_map:
            if s_map[i] % 2 != 0:
                count += 1

        if count > k: 
            return False
        else:
            return True
