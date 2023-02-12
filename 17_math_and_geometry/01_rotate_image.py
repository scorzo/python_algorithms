#!/usr/bin/env python

# ROTATE IMAGE
#
# - given n x n 2d matrix image, rotate image by 90 degrees
# - matrix must be rotated in place
#
# SOLUTION
# - use left and right pointers
# - start upper left top
#
# - while l < r:
#     - for each item in matrix top row, from left to right
#     top, bottom =  l, r
#     # rotate square vertices to the right
#     - save top left into temp var
#     - move bottom left into top left
#     - move bottom right into bottom left
#     - move top left (temp var) into top right
# # move to the next inner concentric square
# r -= 1
# l += 1


import argparse
from typing import List

class Solution:


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


