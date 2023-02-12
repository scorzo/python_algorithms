#!/usr/bin/env python

# PERMUTATIONS (aka PERMUTATIONS W/O REPEATING CHARS)
#
# - given array nums of distinct integers, return distinct permutations
#
# NOTES
#
# - solution uses DFS and backtracking


import argparse
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def dfs(nums, path):
            if not nums:
                ans.append(path)
                return

            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], path + [nums[i]])

        dfs(nums, [])
        return ans

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.permute([1,2,3])  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(answer)

if __name__ == '__main__':
    main()


