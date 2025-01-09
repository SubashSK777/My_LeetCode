class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = math.inf
        max_profit = 0
        curr_profit = 0

        for i in prices:
            if i < mini:
                mini = i
            else:
                profit = i - mini
                max_profit = max(profit, max_profit)

        return max_profit
        