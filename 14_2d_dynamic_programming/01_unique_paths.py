#!/usr/bin/env python

# Dynamic programming is an algorithmic paradigm that divides broader problems into smaller subproblems and stores the result for later use, eliminating the need for any re-computation. This problem-solving approach is quite similar to the divide and conquer approach.
#
# WHY 2D?
#
# I believe this refers to the matrix aspect involved in all of these problems.
#
# UNIQUE PATHS
#
# - calculate all the down/right move only paths from top left to bottom right of m x n grid
# - robot can only move down or right
#
# NOTES
#
# - start bottom right and calculate paths, move left
# - go to second row from bottom, move right to left (by adding bottom and right side values)
# - I believe the proposed solution is considered BOTTOM UP TABULATION form of DYNAMIC PROGRAMMING


import argparse
from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # populate bottom row with 1s

        for i in range(m - 1):
            newRow = [1] * n # tmp placeholder
            for j in range(n - 2, -1, -1): # start, end, increment - goes backwards - starts one back
                newRow[j] = newRow[j + 1] + row[j]  # square = equals right square + bottom square
            row = newRow # make current row the new bottom row
        return row[0]

        # O(n * m) O(n)

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.uniquePaths(3, 7) # 28
    print(answer)

if __name__ == '__main__':
    main()


