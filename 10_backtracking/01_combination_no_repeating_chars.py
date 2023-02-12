#!/usr/bin/env python

# What is BACKTRACKING?
#
# https://www.programiz.com/dsa/backtracking-algorithm
#
# A backtracking algorithm is a problem-solving algorithm that uses a brute force approach for finding the desired output.
#
# The term backtracking suggests that if the current solution is not suitable, then backtrack and try other solutions. Thus, recursion is used in this approach.


# SUBSETS (aka COMBINATION NO REPEATING CHARS)
#
# - look for all possible combinations (not permutations) of numbers within a list
#
# - for each item in the list, you have 2 choices:
#     - include the item in the subset
#     - exclude the item from the subset
#
# - if there are 3 items in the list, then there are 2 ^ 3 possible subsets (or 2 ^ n)
# - complexity is O (n * 2^n)
#
# NOTES
# - with COMBINATIONS, we are just turning values on and off in place (contrary to PERMUTATIONS)
# - solution uses RECURSIVE DFS method
# - subset variable is global and is modified in place as it goes
# - IMPORTANT NOTE subset is shared between DFS calls and the only reason this can happen without race condition is because execution is paused on the first DFS call until it returns - below is the output for reference:
#
#     # i, id, subset
#     0 4496811104 []
#     1 4496811104 [1]
#     2 4496811104 [1, 2]
#     3 4496811104 [1, 2, 3]
#     3 4496811104 [1, 2]
#     2 4496811104 [1]
#     3 4496811104 [1, 3]
#     3 4496811104 [1]
#     1 4496811104 []
#     2 4496811104 [2]
#     3 4496811104 [2, 3]
#     3 4496811104 [2]
#     2 4496811104 []
#     3 4496811104 [3]
#     3 4496811104 []
#     [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]

import argparse
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, subset):
            print(i, id(subset), subset)
            if i == len(nums):
                ans.append(subset)
                return

            dfs(i + 1, subset + [nums[i]])
            dfs(i + 1, subset)

        ans = []
        dfs(0, [])
        return ans

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.subsets([1,2,3]) # [[1,2,3], [1,2], [1,3], [1], [2,3], [2], [3], []]
    print(answer)

if __name__ == '__main__':
    main()


