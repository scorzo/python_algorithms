#!/usr/bin/env python

# SINGLE NUMBER
#
# - given array of integers, find the number that does not show up twice
# - requires linear time complexity and constant extra space
#
# SOLUTION
# - due to memory constraints, you cannot use a hashmap
# - solution is to use bitwise "or" on all of the binary representations of the numbers which will give you the binary value of the number that is unique
# - the reason this happens is that when you do xor on 2 same values, the answer is 0 - so we are eliminating pairs



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


