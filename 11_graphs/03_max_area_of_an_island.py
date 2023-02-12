#!/usr/bin/env python

# MAX AREA OF AN ISLAND
#
# - same setup as above except need to find the max area of any one island
#
# NOTES
# - uses RECURSIVE DFS
# - uses set() to store visited locations


import argparse
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # create results variable
        results = 0

        # create visited set
        visited = set()

        # loop through grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if current location is land and not visited
                if grid[row][col] == 1 and (row, col) not in visited:
                    # call helper function
                    results = max(results, self.dfs(grid, row, col, visited))

        # return results
        return results

    def dfs(self, grid, row, col, visited):
        # if row or col are out of bounds or if current location is water or if current location is visited
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0 or (row, col) in visited:
            # return 0
            return 0

        # add current location to visited set
        visited.add((row, col))

        # call helper function on all 4 directions
        return 1 + self.dfs(grid, row + 1, col, visited) + self.dfs(grid, row - 1, col, visited) + self.dfs(grid, row, col + 1, visited) + self.dfs(grid, row, col - 1, visited)

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],)
    print(answer)

if __name__ == '__main__':
    main()


