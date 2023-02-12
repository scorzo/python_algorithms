#!/usr/bin/env python

# MIN COST CLIMBING STAIRS
#
# similar to climbing stairs:
# - each stair has a cost (ex: 10, 15, 20) to go past it
# - you can take 1 or 2 steps at a time
# - you can start at stair w/ index 0 or w/ index 1
# - how to reach to the top (in other words, go beyond the last step) with the minimal cost
#
# NOTES:
#
# - BRUTE FORCE solution uses DFS DECISION TREE
# - DFS starts at position 0, edges are cost, nodes are number of steps (so 2 choices means a BINARY TREE, each node with 2 child nodes: 1 and 2)
#
# - there is also a DYNAMIC SOLUTION where you reuse calculated values (basically caching)
# - DYNAMIC SOLUTION solves from right to left, using the lesser value of the last 2 slots
# - you can reuse decision tree values from index 0 for index 1 by removing 1st level (remember we have the option of calculating values from index 0 or index 1)

import argparse
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1): # start 3 positions back and go backwards
            cost[i] += min(cost[i + 1], cost[i + 2]) # of the last 2, which is less?

        return min(cost[0], cost[1])

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.minCostClimbingStairs([10, 15, 20])   # 15
    print(answer)

if __name__ == '__main__':
    main()


