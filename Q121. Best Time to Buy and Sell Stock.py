"""
Q121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0
"""

# O(n) runtime, O(1) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        currentBuy = prices[0]
        
        for dayPrice in prices:
            potentialProfit = dayPrice - currentBuy
            if potentialProfit > profit:
                profit = potentialProfit
            if dayPrice < currentBuy:
                currentBuy = dayPrice
        return profit
                