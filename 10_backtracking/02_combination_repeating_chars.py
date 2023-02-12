#!/usr/bin/env python

# COMBINATION SUM (aka COMBINATION W/ REPEATING CHARS)
#
# - similar to SUBSETS problem
# - difference is that we are looking for groups of numbers that total a target
# - also, numbers in the solution can be used more than once
#
# NOTES
#
# - with COMBINATIONS, we are just turning values on and off in place (contrary to PERMUTATIONS)
# - in this case we need to try combinations with repeating numbers - in other words, 2 can be in all the slots (2,2,2,2) but it is always at least in the current position
# - an important thing to note is that any combination on the left side of a node is the only one with that prefix, so the right side of the node changes the prefix by adding the next number in the array to the subset - in other words,
#
# left: 2 2 2 2 3                  right: 2 2 2 2 4
# left 2 2 2 2 3 3  right 2 2 2 2 3 4
#
#
# Note: steps 1 and 2 below can be read as: do this first thing (either add a value or don't) and do this second thing to the next value in line (in this case, for the second step we add the exact same number again)

import argparse
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i, subset, total):
            if total == target:
                ans.append(subset)
                return

            if total > target:
                return

            for j in range(i, len(candidates)):
                dfs(j, subset + [candidates[j]], total + candidates[j])

        ans = []
        dfs(0, [], 0)
        return ans

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.combinationSum([2,3,6,7], 7) # [[2,2,3],[7]]
    print(answer)

if __name__ == '__main__':
    main()


