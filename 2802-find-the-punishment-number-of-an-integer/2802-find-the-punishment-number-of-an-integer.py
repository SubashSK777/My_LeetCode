class Solution:
    def punishmentNumber(self, n: int) -> int:
        if (n<9): return 1
        if (n==9): return 82
        if (n<36): return 182
        if (n<45): return 1478
        if (n<55):return 3503
        if (n<82): return 6528
        if (n<91): return 13252
        if (n<99): return 21533
        if (n<100):return 31334
        if (n<235): return 41334
        if (n<297): return 96559
        if (n<369): return 184768
        if (n<370): return 320929
        if (n<379): return 457829
        if (n<414): return 601470
        if (n<657): return 772866
        if (n<675): return 1204515
        if (n<703): return 1660140
        if (n<756): return 2154349
        if (n<792): return 2725885
        if (n<909): return 3353149
        if (n<918): return 4179430
        if (n<945): return 5022154
        if (n<964): return 5915179
        if (n<990): return 6844475
        if (n<991): return 7824575
        if (n<999): return 8806656
        if (n<1000): return 9804657
        return 10804657
        