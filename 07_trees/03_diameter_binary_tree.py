#!/usr/bin/env python

# DIAMETER OF A BINARY TREE
#
# - the diameter of a binary tree is the length of the longest path between any two nodes in a tree (represented by number of edges between the two)
#
# NOTES
#
# - uses DFS with operational time complexity (n) because we only need to look at each node once
# - we need to count edges in order to get the diameter
# - for each node we need to get the longest left and right paths and add them together
# - one way to do that is to add the left path to the right path value and then add 2 (one edge for each direction (left and right))
#
#
# - DFS function
# - starts at bottom
# - empty nodes at bottom return -1
# - first we get the diameter for the node at this point by:
#     - getting the recursive call's return value for both left and right
#     - adding them together
#     - adding 2 (to account for the 2 edges above the left and right paths)
#     - note that the adding 2 at the bottom is cancelled out by the "empty nodes at bottom return -1" in the event that the node has empty nodes
#
# - next we need to track what the max diameter is at every DFS function call on each node using a max() function and a global variable (res=[0]) - note that we use an array since the value needs to be mutable


import argparse
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.diameterOfBinaryTree()
    print(answer)

if __name__ == '__main__':
    main()


