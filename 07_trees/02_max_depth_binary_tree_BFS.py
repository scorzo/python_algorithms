#!/usr/bin/env python

# MAXIMUM DEPTH OF BINARY TREE
#
# - find max depth of binary tree (path to leaf with most nodes
#
# - BREADTH FIRST
#
# - use deque() to cache nodes - it has a log(1) operational time complexity for popping left vs. a list which is log(n)
#
# NOTES:
#
# - add root node to queue
# - while nodes in queue:
#     for all nodes in queue:
#         pop node off queue
#         add left node to queue
#         add right node to queue
#     increment layer counter

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
        q = deque()
        if root:
            q.append(root)

        level = 0

        while q:

            for i in range(len(q)): # snapshot
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

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


