class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        hash1 = Counter(s1)
        hash2 = Counter(s2)
        lens = len(s1)

        if hash1 != hash2:
            return False

        count = 0

        for i in range(lens):
            if s1[i] == s2[i]:
                continue
            else:
                count += 1

        return count <= 2