#!/usr/bin/env python

# BINARY SEARCH
#
# - find index of target in sorted list
# - must have O (log n) runtime complexity
#
# NOTES
# - uses 2 POINTERS, left and right
# - until you find the target:
# - find middle index and see if target above or below that point
# - if target greater than value at index, move right pointer to the left of the middle
# - if target below...
# - if target matches, return as found


import argparse
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.search([-1,0,3,5,9,12], 9)
    print(answer)

if __name__ == '__main__':
    main()


