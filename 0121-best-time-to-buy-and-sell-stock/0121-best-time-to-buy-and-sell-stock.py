class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        profit = 0
        maxProfit = 0
        for i in range(len(prices)):
            minPrice = min(prices[i],minPrice)
            profit = prices[i]-minPrice
            maxProfit = max(profit,maxProfit)
        return maxProfit
        