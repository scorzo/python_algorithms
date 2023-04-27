#!/usr/bin/env python

# - given array of ints sorted increasing order, return indices of 2 numbers that add up to target value
#
# NOTES
#
# - iterate left (increment) and right pointers (decrement) together
# - on each iteration, sum of 2 values is less than or greater than target
# - if less than, increment left pointer since the array is sorted and that will increase the value
# - if greater than target, do the opposite

import argparse
from typing import List





class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.twoSum()
    print(answer)

if __name__ == '__main__':
    main()


