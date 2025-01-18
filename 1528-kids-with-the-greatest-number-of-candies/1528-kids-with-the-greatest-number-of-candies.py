class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n_candies = candies.copy()
        res = []
        n = len(candies)

        for i in range(n):
            n_candies[i] += extraCandies
            if n_candies[i] >= max(candies):
                res.append(True)
            else:
                res.append(False)

        return res
        