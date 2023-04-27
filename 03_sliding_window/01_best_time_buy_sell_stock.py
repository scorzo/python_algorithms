#!/usr/bin/env python

# - given a graph of plotted points,
# - return the maximum profit from buying and selling one transaction pair
#
# NOTES
#
# - uses 2 pointers
# - l starts on 0, r starts on 1
# - until r gets to the end of the list:
# - if l is less than r, record profit if highest so far and move r + 1
# - otherwise, shift l and r to the right by 1


import argparse
from typing import List





class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.maxProfit([7,1,5,3,6,4])
    print(answer)

if __name__ == '__main__':
    main()


