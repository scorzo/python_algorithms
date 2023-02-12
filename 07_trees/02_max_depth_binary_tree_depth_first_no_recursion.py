#!/usr/bin/env python

# MAXIMUM DEPTH OF BINARY TREE
#
# - find max depth of binary tree (path to leaf with most nodes
#
# - DEPTH FIRST WITHOUT RECURSION (ITERATIVE)
#
# - seems to be exactly like DFS RECURSION except that it is using a while loop and a stack (just a list of lists [[node,depth]] rather than function calls


import argparse
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.maxDepth()
    print(answer)

if __name__ == '__main__':
    main()


