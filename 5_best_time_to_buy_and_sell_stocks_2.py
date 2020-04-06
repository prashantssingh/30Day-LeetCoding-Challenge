# PROBLEM DESCRIPTION:
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (i.e., buy one and sell one share of the stock multiple times).
# 
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
# 
# EXAMPLES:
# INPUT:                                                OUTPUT: 
# [7,1,5,3,6,4]                                         7
# EXPLANATION: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# 
# INPUT:                                                OUTPUT: 
# [1,2,3,4,5]                                           4
# EXLANATION: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# 
# INPUT:                                                OUTPUT: 
# [7,6,4,3,1]                                           0
# EXPLANATION: In this case, no transaction is done, i.e. max profit = 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: 
            return 0
        
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
                
        return profit