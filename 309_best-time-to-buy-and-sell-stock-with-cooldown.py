# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
def maxProfit(prices):
    sold, held, reset = float('-inf'), float('-inf'), 0

    for price in prices:
        # Alternative: the calculation is done in parallel.
        # Therefore no need to keep temporary variables
        #sold, held, reset = held + price, max(held, reset-price), max(reset, sold)

        pre_sold = sold
        sold = held + price
        held = max(held, reset - price)
        reset = max(reset, pre_sold)

    return max(sold, reset)
    
#         p_len = len(prices)
#         if p_len <= 1:
#             return 0
#         if p_len == 2 and prices[1] > prices[0]:
#             return prices[1] - prices[0]
#         elif p_len == 2 and prices[1] <= prices[0]:
#             return 0
        
#         dp = [[0 for x in range(2)] for y in range(p_len)] 
#         dp[0][0] = 0
#         dp[0][1] = -prices[0]
#         dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
#         dp[1][0] = max(dp[0][1], dp[0][0] - prices[1])
        
#         for i in range(2, p_len):
#             dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
#             dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
            
#         return dp[p_len-1][0]

assert(maxProfit([1,2,3,0,2])) == 3
assert(maxProfit([1,3,4])) == 3