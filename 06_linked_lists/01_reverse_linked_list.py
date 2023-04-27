#!/usr/bin/env python

# REVERSE LINKED LIST
#
# - take a linked list and reverse the order
# - python does not have a linked list type - you need to build a short class
#
# # reversing
# - initial solution is ITERATIVE solution and uses 2 POINTERS
# - pointers are "previous" and "current"
# - cache the node that current is pointing to
# - point current to previous (in other words swing pointer around)
# - shift both pointers to the right and repeat
# - time complexity: T 0(n) and memory complexity M 0(1)
#
# - RECURSIVE solution
# - T 0(n) and M 0(n) so less efficient



import argparse
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # create tmp node
        prev, curr = None, head

        while curr:
            tmp = curr.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.reverseList()
    print(answer)

if __name__ == '__main__':
    main()


