class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flow = [0] + flowerbed + [0]

        for i in range(1, len(flow) - 1):
            if flow[i] == 0 and flow[i - 1] == 0 and flow[i + 1] == 0:
                flow[i] = 1
                n -= 1
        return n <= 0
        