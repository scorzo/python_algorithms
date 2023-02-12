#!/usr/bin/env python

# LONGEST COMMON SUBSEQUENCE
#
# - return the longest common subsequence between 2 strings
# - a subsequence is a new string generated from a string with some or none characters deleted without changing the order of the characters
#
# NOTES
#
# - this uses a 2D grid (matrix) to solve it (which is why it's considered a 2D DP problem)
# - define boundary of matrix with zeroes
# - grid is labelled with one word across and one down
#
# # first part of video shows us how values are calculated based on matches - I.E.,
#
# - start upper left
# - if letter matches, go diagonally
# - if no match, go both right and left
#
# - when you get to the end of a path, add values backwards until you get to start position 0,0 as follows:
# - diagonals (matches) are worth 1
# - non matches (i.e., up or down) are 0, so just move the existing total without modifying it
#
# # based on the background info below, we solve our problem with a BOTTOM UP approach as follows - this is the DYNAMIC PROGRAMMING part:
#
# - start from bottom right square
# - if it's a col/row match, add (1 + the down right diagonal value) to the total
# - if it's not a col/row match, populate square w/ max of left square and bottom square
# - now move position to one square to the left


import argparse
from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.longestCommonSubsequence("abcde", "ace")  # 3
    print(answer)

if __name__ == '__main__':
    main()


