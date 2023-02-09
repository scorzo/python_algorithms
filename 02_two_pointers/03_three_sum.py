#!/usr/bin/env python

# - given int array, return all triplets where numbers are unique and values add up to 0
#
# NOTES
#
# - similar to two pointers
# - idea is to cycle through all the numbers in the list in sorted order
# - for each list item, run 2 pointers on the range to the right of the number (so it's kind of like 3 pointers)

import argparse
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.threeSum([-1,0,1,2,-1,-4])
    print(answer)

if __name__ == '__main__':
    main()


