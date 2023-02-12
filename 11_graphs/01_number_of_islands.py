#!/usr/bin/env python

# NUMBER OF ISLANDS
#
# - find the number of islands (made up of 1s) in a rectangular matrix
#
# NOTES
#
# - use a SET ( visit = set() ) to mark positions visited using x and y coords
# - use BFS (breadth first search)
# - BFS is not recursive, it's iterative, so we need a data structure to use for memory; in this case what that means is that BFS will run once per island and iterate over a queue - this is a list of matrix positions that haven't been visited yet:
# - a queue is usually used for BFS
#     collections.deque()
# - queue starts with one position: 0,0
# - loop applies 4 coordinate transforms (up down left right) to the position - if it any of them have a value of 1, then they are added to the queue (unless it's already in the visit set)
#                                                                                                                                                               - item is added to the visit set


import argparse
from typing import List

class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
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
                    self.bfs(grid, row, col, visited)
                    # increment results
                    results += 1

        # return results
        return results

    def bfs(self, grid, row, col, visited):
        # create queue
        queue = [(row, col)]

        # loop through queue
        while queue:
            # pop first item from queue
            row, col = queue.pop(0)

            # if current location is land and not visited
            if grid[row][col] == 1 and (row, col) not in visited:
                # add current location to visited set
                visited.add((row, col))

                # add all 4 directions to queue
                if row + 1 < len(grid):
                    queue.append((row + 1, col))
                if row - 1 >= 0:
                    queue.append((row - 1, col))
                if col + 1 < len(grid[0]):
                    queue.append((row, col + 1))
                if col - 1 >= 0:
                    queue.append((row, col - 1))

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.numIslands([[0,0,1,0,0,0,0,1,0,0,0,0,0],)
    print(answer)

if __name__ == '__main__':
    main()


