class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        map = defaultdict(int)

        bal_map = {}
        col_map = {}

        res = []

        for ball, color in queries:
            if ball in bal_map:
                prev = bal_map[ball]
                col_map[prev] -= 1
                if col_map[prev] == 0:
                    del col_map[prev]

            bal_map[ball] = color
            col_map[color] = col_map.get(color, 0) + 1
            res.append(len(col_map))

        return res
        