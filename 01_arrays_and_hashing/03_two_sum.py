#!/usr/bin/env python

# - given array of integers and a target, return 2 indices that add up to target

# NOTES
#
# 1) brute force:
#
#     - for each value in list, compare to every other value in list
#     - as you go right, you only need to compare the current number to numbers on the right
#     - time complexity of O (n^2)
#
#
# 2) use subtraction:
#
#     - go through all values in array
#     - do (target - value) and check if difference exists as a value in hashmap
#     - if yes, you have the answer
#     - if no, add value and index to hashmap and move to next one in line doing the same steps
#
#     - has time and mem complexity of: O(n)

import argparse
from typing import List



# given list of ints and target, return 2 indices that add up to target



class Solution:
    # subtraction method
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums:
                return [i, nums.index(diff)]

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.twoSum([2,7,11,15], 9)
    print(answer)

if __name__ == '__main__':
    main()


