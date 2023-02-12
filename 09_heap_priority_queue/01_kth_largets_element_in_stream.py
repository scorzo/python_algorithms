#!/usr/bin/env python

# Kth LARGEST ELEMENT IN A STREAM
#
# - write class where you can add an integer to a list and have the list return the k largest element
# - adding an item to an array requires O (n) time since you may need to potentially copy n elements in order to make room for the new one
# - a HEAP data structure allows you to insert items into a sorted list in O (log n) time
# - HEAP data structure allows for retrieving min value in O (1) time
#
# SOLUTION:
#
# - init the constructor with:
#     - list of ints
#     - k value
#
# - convert list to heap with heapq.heapify(self.minHeap)
#     - while minHeap is longer than k places, truncate heap to k places using heapq.heappop(self.minHeap) - this is the "min" part of minHeap
#
# - add function:
# use heapq.heappush(self.minHeap, val)
# heapq.heappop(self.minHeap)


import argparse
from typing import List

class Solution:
    def __init__(self, nums: List[int], k: int):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

def main():
    # Use argparse to handle command line arguments
    parser = argparse.ArgumentParser(description='A basic Python script template.')
    parser.add_argument('-a', '--arg1', type=str, help='An example argument')
    args = parser.parse_args()

    # call here
    solution = Solution()
    answer = solution.add(3)    # 3
    print(answer)

if __name__ == '__main__':
    main()


