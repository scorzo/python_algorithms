#!/usr/bin/env python

# Dynamic programming is an algorithmic paradigm that divides broader problems into smaller subproblems and stores the result for later use, eliminating the need for any re-computation. This problem-solving approach is quite similar to the divide and conquer approach.
#
# CLIMBING STAIRS
#
# how many ways can you combine 1 and 2 steps to get up a set of n stairs?
#
# NOTES
#
# - use a decision tree
# - you could use BFS, but if you use DFS, then you can cache the values to reduce the work
# - use a technique where you start at the end of the DFS decision tree and add the last 2 values going backwards
# - instead of using a list to store the values going backwards, you technically only need the last 2 positions which reduces the memory footprint (see video for more)


import argparse
from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.climbStairs(5) # 8
    print(answer)

if __name__ == '__main__':
    main()


