#!/usr/bin/env python

# SPIRAL MATRIX
#
#
# SOLUTION
# - use a results[] array
# - use boundary pointers
# - every time you complete a row or column, move the boundary pointer on the top/bottom or side in towards the center
# - when the boundary pointers overlap in either direction, you are through



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


