#!/usr/bin/env python

# REORDER LIST
#
# - given a linked list, reorder the list by inserting n-1 list item into position 2, n-2 into position 4, etc.
# - do not return anything
# - modify list in place


# left hand



#
# NOTES
#
# - divide list into 2 parts
# - if list is odd number, then the middle node will go into second list
# - note that in the video he uses a slow/fast pointer technique to split the lists instead of the method above - makes sense since this is not an array where we can get count nodes
# - reverse second list (see REVERSE LINKED LIST technique above)
# - merge 2 lists (sort of like MERGE 2 LINKED LISTS above)
#
# # merging
# - take 2 linked lists
# - cache 2nd item in each list
# - move pointers to first items in each list
# - point first list item in first list down to 2nd list
# - point first list item in second list up and diagonally to the right to the 2nd item first list
# - move pointers to 2nd items in each list
# - repeat


import argparse
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
         # find middle
         # reverse second half
         # merge first and second halves

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second.next:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second.next:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2





















class Solution:
    def reorderList(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next # use second instead of slow
        prev = slow.next = None # break the chain
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.reorderList()
    print(answer)

if __name__ == '__main__':
    main()


