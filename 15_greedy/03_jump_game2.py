#!/usr/bin/env python

# JUMP GAME II
#
# - same as jump game 1:
# - given array of integers
# - get from index 0 to the last index
# - integers represent max number of steps you can take from that position
#
# - difference is:
# - all integers are non negative
# - also, you need to come up with the least amount of jumps to get to the last index
#
# DYNAMIC PROGRAMMING SOLUTION
#
# - O(n^2) time solution
# - the values can be represented as a DECISION TREE - for example...
#     input array: [ 2 3 1 2 ]
#     2
# 3    1
# 1 2   2
# - each level in the DECISION TREE represents the number of steps - for example, level 3 would be 2 steps
# - the values in the levels will have overlap - for example index 2, value 1 is in 2 levels, so it could be step 1 or step 2
#
#
#
# GREEDY SOLUTION (BFS)
#
# - linear time solution O(n)
# - use LEFT and RIGHT POINTERS (SLIDING WINDOW) to track which level we are on at any moment
# - in the GREEDY solution, we set the right pointer to the right of itself when going down a level - in other words, there will be no overlap in levels (as described above)
# - this solution is BFS on a 1 DIMENSIONAL ARRAY


import argparse
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.jump([2,3,1,1,4]) # 2
    print(answer)

if __name__ == '__main__':
    main()


