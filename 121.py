class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        for i in range(len(prices)):
            for x in range(i+1, len(prices)):
                if prices[i] >= prices[x]:
                    break
                profits.append(prices[x] - prices[i])
        if profits:
            return max(profits)
        else: 
            return 0
                