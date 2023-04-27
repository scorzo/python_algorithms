#!/usr/bin/env python

# MAXIMUM DEPTH OF BINARY TREE
#
# - find max depth of binary tree (path to leaf with most nodes
#
# - DEPTH FIRST WITH RECURSION (T 0(n))
#
# - the DFS function gets called on each node
# - note that the recursive function calls cannot start returning values until they reach a pair of nodes for which both nodes return 0 - so the counting starts at the bottom of the tree and works its way up



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
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

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


