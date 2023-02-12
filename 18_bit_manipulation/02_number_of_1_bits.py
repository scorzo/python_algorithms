#!/usr/bin/env python

# NUMBER OF 1 BITS
#
# SOLUTION
# 2 ways to do this both with same time complexity:
#
#     1) do modulus 2 on binary number which returns 1 if it's a 1 and 0 otherwise
#     2) if modulus returns 1, then increment the total by 1
#     3) right shift number with >> which removes the digit from the right and adds it to the left
#     4) run steps 1 thru 3 until you've cycled all the digits
#
#     2nd way:
#         - uses n = n & (n - 1) #


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


