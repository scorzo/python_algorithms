#!/usr/bin/env python

# SEARCH 2D MATRIX
#
# - find target in SORTED VALUE matrix
# - solution is a double binary search: get the middle row and see if target is there - if not, remove rows above or below accordingly - once you pin it down to a row, use binary search from example above (BINARY SEARCH)
# - solution is 0(log m + log n) - note: the log n part is the binary search from above - in the log m part, m is the rows


import argparse
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # hone in on the row
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False

        # hone in on the col
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)  # True
    print(answer)

if __name__ == '__main__':
    main()


