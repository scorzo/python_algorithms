#!/usr/bin/env python

# BEST TIME TO BUY AND SELL STOCK WITH COOLDOWN
#
# - given a list of stock prices, find the optimal buy/sell/cooldown pattern where you must cooldown for at least one day after any sell day
#
# NOTES
# - uses DFS
# - uses HASHMAP for caching "seen" decisions
# - HASHMAP key is a tuple # key=(i, buying) val=max_profit
# - so, the HASHMAP contains the max_profit at i and will continually get
# - we start at the beginning of the list and (using DFS) we calculate every single possible path going forward
#
# - if you buy, your max_profit goes down on that day
# - if you sell, your max_profit goes up on that day
# - pause and it stays the same


import argparse
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying) # just means pause for a day
            if buying:
                # sell the next day or pause the next day
                buy = dfs(i + 1, False) - prices[i] # tomorrow sell price outcome - today price
                dp[(i, True)] = max(buy, cooldown)
            else:
                # buy in 2 days or pause the next day
                sell = dfs(i + 2, True) + prices[i]
                dp[(i, False)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.maxProfit([7,1,5,3,6,4])  # 7
    print(answer)

if __name__ == '__main__':
    main()


