#!/usr/bin/env python

# JUMP GAME
#
# SOLUTION
#
# - can be solved either DYNAMICALLY or in GREEDY way
#
# DYNAMIC PROGRAMMING SOLUTION:
# - nodes are indexes
# - create a DECISION TREE where the nodes are the indexes where you land, and the edges represent the different jump options (so for a value of 3, it would be 1,2 and 3)
# - create a "cache" using an array called DP (DYNAMIC PROGRAMMING) where you store true or false - i.e., the end can be reached from that index:
# - example: dp[2] = false
#
# GREEDY SOLUTION
# - avoids having to use a decision tree and a cache
# - start by setting your goalpost to the last index of the input array
# - idea is to move goalpost as far left as possible until you reach the start


import argparse
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 # set goal to last one

        for i in range(len(nums) - 2, -1, -1): # start second to last working backwards
            if i + nums[i] >= goal:  # does adding this value get us past the goal?
                goal = i # move goalpost to the left
        return goal == 0 # did we get goalpost to 0 index?

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.canJump([2,3,1,1,4])  # true
    print(answer)

if __name__ == '__main__':
    main()


