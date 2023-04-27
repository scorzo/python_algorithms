#!/usr/bin/env python

# MERGE 2 LINKED LISTS
#
# - merge 2 SORTED, LINKED LISTS into a single list IN ORDER
#
# NOTES
# - this requires 3 "holders":
# 1) temp var, aka "tail", which will be a starting point for our combined linked list - this var is moved along combined linked list and always points to the last node we added
#
# 2 & 3) list1 and list2 point to the respective heads of the 2 lists we are working with - each time we point tail to either list1 or list2, we update the respective variable its "next" node - we use these to do the value comparisons we use to determine which one will be next in out tail list
#
# - start by creating a new, dummy node
#
#
# - use 2 variables (list1 and list2) to hold first (lowest value) node from each list
# - while 2 variables contain node references,
# - compare values


import argparse
from typing import List







# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.mergeTwoLists()
    print(answer)

if __name__ == '__main__':
    main()


