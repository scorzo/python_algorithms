#!/usr/bin/env python

# HOUSE ROBBER
#
# - given list of values
# - return highest total value you can get by adding values - but none of the indexes can be touching
#
# NOTES
#
# - introduces RECURRANCE RELATIONSHIP which is a way to break up DYNAMIC PROGRAMMING problems
# - trick is to break the problem into subsets, calculate the highest totals from those groups and store those values somewhere (so that you don't need to recalculate over and over)
#
# example:
#
# 1 2 3 4  # input array
# 1        # highest total from first col
# 2      # highest total from first 2 cols
# 4    # highest total from first 3 cols
# 4  # highest total from first 4 cols # note that is going to be max value from col3 or col2 + col4
#
# aka: col4 = max(col3, col2+col4)


import argparse
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.rob([1,2,3,1])    # 4
    print(answer)

if __name__ == '__main__':
    main()


