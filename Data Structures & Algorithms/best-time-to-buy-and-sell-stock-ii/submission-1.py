class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxiprof = 0
        for i in range(1, len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            elif prices[i] - mini > 0:
                maxiprof += prices[i] - mini
                mini = prices[i]
        return maxiprof