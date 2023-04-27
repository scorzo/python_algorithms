#!/usr/bin/env python

# INVERT BINARY TREE
#
# NOTES
# - binary tree requires a simple TreeNode class with 3 attributes: value, left node, right node
# - it's more like a horizontal flip
# - swap pointers (need to cache one of the pointer values in tmp var to do this)
# - solution is RECURSIVE - uses DFS - note that even though we are not "searching", it's still called DFS
#
# PSEUDO CODE:
#
# - swap function:
    # - copy node.left contents into tmp var
    # - redirect node.left pointer to contents of node.right
    # - redirect node.right pointer to contents of tmp var
    #
    # - run swap function on node.left
    # - run swap function on node.right
#
# - run swap function on root node


import argparse
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.invertTree()
    print(answer)

if __name__ == '__main__':
    main()


