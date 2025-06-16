class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        s1_map = Counter(s1)
        window = Counter(s2[:n])

        if window == s1_map:
            return True

        for i in range(n, m):
            window[s2[i]] += 1
            window[s2[i - n]] -= 1
            if window[s2[i - n]] == 0:
                del window[s2[i - n]]
            if window == s1_map:
                return True
        return False
