#!/usr/bin/env python

# WHAT IS A GREEDY ALGORITHM?
#
# https://www.techopedia.com/definition/16931/greedy-algorithm
#
# A greedy algorithm works by choosing the best possible answer in each step and then moving on to the next step until it reaches the end, without regard for the overall solution. It only hopes that the path it takes is the globally optimum one, but as proven time and again, this method does not often come up with a globally optimum solution. In fact, it is entirely possible that the most optimal short-term solutions lead to the worst possible global outcome.
#
# Think of it as taking a lot of shortcuts in a manufacturing business: in the short term large amounts are saved in manufacturing cost, but this eventually leads to downfall since quality is compromised, resulting in product returns and low sales as customers become acquainted with the “cheap” product. But this is not always the case, there are a lot of applications where the greedy algorithm works best to find or approximate the globally optimum solution such as in constructing a Huffman tree or a decision learning tree.
#
#
# MAXIMUM SUBARRAY
#
# - find max total of any contiguous array values in a list
#
# NOTES
#
# - one solution is brute force
# - another solution is similar to SLIDING WINDOW


import argparse
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0] # start w/ value from first index

        total = 0
        for n in nums:
            total += n # keep increasing total
            res = max(res, total) # track the maximum total so far
            if total < 0: # if total goes below 0, set it to 0
                total = 0
        return res

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])  # 6
    print(answer)

if __name__ == '__main__':
    main()


